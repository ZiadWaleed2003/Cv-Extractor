from PIL import Image, ImageFilter, ImageEnhance
import pdf



def preprocess_image_for_ocr(image):
    """
    Preprocess image to improve OCR accuracy using PIL only.
    
    Args:
        image: PIL Image object
        
    Returns:
        PIL Image: Preprocessed image
    """
    # Convert to grayscale
    if image.mode != 'L':
        image = image.convert('L')
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    
    # Enhance sharpness
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(2.0)
    
    # Apply a slight blur to reduce noise
    image = image.filter(ImageFilter.MedianFilter(size=3))
    
    # Apply unsharp mask for better edge definition
    image = image.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))
    
    return image



def extract_text_with_ocr(file_path, dpi=300, lang='eng'):
    """
    Extract text from scanned PDF using OCR.
    
    Args:
        file_path: Path to the PDF file
        dpi: DPI for image conversion (higher = better quality but slower)
        lang: Language for OCR (default: English)
        
    Returns:
        str: Extracted text content
    """
    try:
        # Convert PDF pages to images
        print("Converting PDF to images...")
        pages = pdf2image.convert_from_path(file_path, dpi=dpi)
        
        extracted_text = ""
        
        for i, page in enumerate(pages):
            print(f"Processing page {i + 1}/{len(pages)}...")
            
            # Preprocess the image for better OCR
            processed_page = preprocess_image_for_ocr(page)
            
            # OCR configuration for better results
            custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;:!?()[]{}"\'-/@#$%^&*+=<>|~`_ '
            
            # Extract text from the image
            page_text = pytesseract.image_to_string(
                processed_page,
                lang=lang,
                config=custom_config
            )
            
            if page_text.strip():
                extracted_text += page_text + "\n"
        
        return extracted_text.strip()
    
    except Exception as e:
        print(f"Error extracting text with OCR: {e}")
        return ""