import pdfplumber
import re

def is_text_based_pdf(file_path : str, min_text_length=100, min_words=10) -> bool:
    """
    Determine if the uploaded CV is text-based or scanned PDF.
    
    Args:
        file_path: Path to the CV file
        min_text_length: Minimum character count to consider text-based
        min_words: Minimum word count to consider text-based
    
    Returns:
        bool: True if text-based, False if scanned
    """
    try:
        with pdfplumber.open(file_path) as pdf:
            total_text = ""
            
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    total_text += text.strip()
            
            # Check if we have meaningful text content
            if len(total_text) >= min_text_length:
                # Count actual words (not just whitespace/special chars)
                words = re.findall(r'\b\w+\b', total_text)
                return len(words) >= min_words
            
            return False
    except Exception as e:
        print(f"Error checking PDF type: {e}")
        return False
    

def extract_text_from_pdf(file_path : str) -> str:
    """
    Extract text from a text-based PDF.
    
    Args:
        file_path: Path to the PDF file
        
    Returns:
        str: Extracted text content
    """
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""
    

