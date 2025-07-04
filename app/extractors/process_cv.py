from extractors.pdf_utils import is_text_based_pdf , extract_text_from_pdf

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
        return extract_text_from_pdf(file_path)
    else:
        print("Processing scanned PDF with OCR...")
        return extract_text_with_ocr(file_path)  # You'll need to implement this