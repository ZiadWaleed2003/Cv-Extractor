from app.agents.client import get_llm , get_llm_client


class Scrutinizer:

    def __init__(self):
        
        self.client = get_llm_client()
        self.model  = get_llm()
        self.system_prompt = self._create_sys_prompt()


    def _create_sys_prompt(self):
        sys_prompt = "".join([
            "You are a Senior Technical Recruiter with 10+ years of experience in talent acquisition. ",
            "Your task is to evaluate a candidate's CV against specific job requirements and provide a comprehensive assessment with a clear hire/no-hire recommendation.\n\n",
            
            "**Input:** ",
            "- Extracted CV text ",
            "- Job requirements\n\n",
            
            "**Evaluation Criteria:**\n",
            "1. **Experience** (30%): Relevant work experience, years in field, progression, technologies used\n",
            "2. **Projects** (25%): Technical complexity, relevance, impact, problem-solving approach\n",
            "3. **Education** (20%): Degree relevance, institution quality, additional certifications\n",
            "4. **CGPA/Academic Performance** (15%): Academic excellence indicator\n",
            "5. **Skills Match** (10%): Technical skills alignment with requirements\n\n",
            
            "**Output Format:**\n",
            "- **Overall Score:** X/10\n",
            "- **Recommendation:** HIRE/NO HIRE/MAYBE (with clear reasoning)\n",
            "- **Strengths:** Top 3 candidate strengths\n",
            "- **Weaknesses:** Areas of concern\n",
    
            "**Guidelines:**\n",
            "- Be objective and evidence-based\n",
            "- Consider both hard and soft skills\n",
            "- Account for career level and growth potential\n",
            "- Highlight red flags if any\n",
            "- Provide actionable feedback\n\n",
            
            "Maintain a professional, balanced tone throughout your assessment."
        ])
    
        return sys_prompt
    

    def judge_candidate(self, requirements, cv_json):
        try:
            user_prompt = "".join([
                "Please judge this candidate's CV according to the provided instructions.\n\n",
                "**JOB REQUIREMENTS:**\n",
                f"{requirements}\n\n",
                "**CANDIDATE CV (JSON FORMAT):**\n",
                f"{cv_json}\n\n",
                "Please provide your assessment following the specified output format."
            ])
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0
            )
            
            assessment = response.choices[0].message.content
            
            if not assessment or len(assessment.strip()) < 100:
                raise ValueError("Received incomplete assessment response")
                
            return assessment
            
        except Exception as e:
            print(f"Error in judge_candidate: {e}")
            raise ValueError(f"Failed to get LLM response: {e}")
          



