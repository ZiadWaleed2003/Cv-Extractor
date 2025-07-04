from PIL import Image, ImageFilter, ImageEnhance
import pytesseract
import fitz
import tempfile
import os


def preprocess_image_for_ocr(image):
    """
    Preprocess image to improve OCR accuracy.
    
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
    Extract text from scanned PDF using OCR with PyMuPDF.
    
    Args:
        file_path: Path to the PDF file
        dpi: DPI for image conversion (higher = better quality but slower)
        lang: Language for OCR (default: English)
        
    Returns:
        str: Extracted text content
    """
    try:
        print("Converting PDF to images using PyMuPDF...")
        extracted_text = ""
        
        with fitz.open(file_path) as doc:
            for i, page in enumerate(doc):
                print(f"Processing page {i + 1}/{len(doc)}...")
                
                # Convert page to pixmap (image)
                pix = page.get_pixmap(dpi=dpi)
                
                # Create temporary image file
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_img:
                    img_path = temp_img.name
                    pix.save(img_path)
                    
                    # Open image with PIL
                    img = Image.open(img_path)
                    
                    # Preprocess the image for better OCR
                    processed_img = preprocess_image_for_ocr(img)
                    
                    # OCR configuration for better results
                    custom_config = r'--oem 3 --psm 6'
                    
                    # Extract text from the image
                    page_text = pytesseract.image_to_string(
                        processed_img,
                        lang=lang,
                        config=custom_config
                    )
                    
                    if page_text.strip():
                        extracted_text += page_text + "\n"
                    
                    # Clean up temporary file
                    os.remove(img_path)
        
        return extracted_text.strip()
    
    except Exception as e:
        print(f"Error extracting text with OCR: {e}")
        return ""