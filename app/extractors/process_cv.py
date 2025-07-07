from app.extractors.pdf_utils import is_text_based_pdf
from app.extractors.image_extractor import ImageExtractor
from app.extractors.text_extractor import TextExtractor

def process_cv(file_path):
    """
    Main function to process CV based on its type.
    
    Args:
        file_path: Path to the CV file
        
    Returns:
        str: Extracted text content
    """
    if is_text_based_pdf(file_path):
        print("Processing text-based PDF...")
        text_ext = TextExtractor()

        return text_ext.extract_text_from_pdf(file_path)
    else:
        print("Processing scanned PDF with OCR...")

        img_ext = ImageExtractor()
        return img_ext.extract_text_with_ocr(file_path)