import openai
import os
import json
from data_model import ParsedCV
from client import get_llm , get_llm_client

class CvParser:
    def __init__(self):
        self.client = get_llm_client()
        
        self.model = get_llm()
        self.system_prompt = self._create_system_prompt()
    
    def _create_system_prompt(self) -> str:
        """Create the system prompt for CV parsing"""

        sys_prompt = "".join([
            "You are a professional CV/Resume parser. ",
            "Your task is to extract structured information from CV text and return it in a specific JSON format",
            "INSTRUCTIONS:",
            "1. Parse the provided CV text carefully and extract all relevant information"
            "2. Structure the data according to the provided JSON schema",
            "3. If information is not available, use null or empty arrays as appropriate",
            "4. Be precise with dates - use YYYY-MM or YYYY format",
            "5. Extract skills as individual items, not grouped categories",
            "6. For experience and education, maintain chronological order (most recent first)",
            "7. Clean and normalize the data (remove extra whitespace, fix formatting)",
            "8. If a field is unclear or ambiguous, make your best interpretation",
            "RESPONSE FORMAT:",
            f"Return ONLY a valid JSON object that matches this schema```json\n" + json.dumps(ParsedCV.model_json_schema())+ "```\n. Do not include any additional text, explanations, or markdown formatting.",

        ])

        return sys_prompt 

    def parse_cv(self, cv_text: str) -> ParsedCV:
        """
        Parse CV text and return structured data
        
        Args:
            cv_text (str): Raw CV text content
            
        Returns:
            ParsedCV: Parsed and structured CV data
        """
        try:
            # Create the user prompt with CV text
            user_prompt = "".join([
                        "Please parse the following CV text and extract all relevant information:",
                        f"{cv_text}",
                        "Return the extracted information as a JSON object following the ParsedCV schema."
                    ])

            # Make API call to LLM
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0,  # Low temperature for consistent parsing
                response_format={"type": "json_object"}
            )
            
            # Extract and parse the JSON response
            json_response = response.choices[0].message.content
            parsed_data = json.loads(json_response)
            
            # Validate and return as Pydantic model
            return ParsedCV(**parsed_data)
                  
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse LLM response as JSON: {e}")
        except Exception as e:
            raise RuntimeError(f"Error parsing CV: {e}")
        
    

    def save_cv_to_json(self, cv_text: str, filename: str) -> None:
        """
        Parse CV text and save to JSON file
        
        Args:
            cv_text (str): Raw CV text content
            filename (str): Output JSON filename
        """
        parsed_cv = self.parse_cv(cv_text)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(parsed_cv.model_dump(), f, indent=2, ensure_ascii=False)
        
        print(f"CV saved to {filename}")