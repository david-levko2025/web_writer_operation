import pytesseract
from PIL import Image

class OCREngine:
    def extract_text(self, image_path: str) -> str:
        try:
            with Image.open(image_path) as img:
                return pytesseract.image_to_string(img).strip()
        except Exception as e:
            print(f"ocr Error: {e}")
            return ""