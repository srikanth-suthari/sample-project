import pytesseract
from PIL import Image, ImageFilter

# Set Tesseract path for macOS
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

try:
    # Open and preprocess the image
    image = Image.open("/Users/srikanth/test-dir/captcha.png")
    image = image.filter(ImageFilter.SHARPEN)
    image = image.convert("L")
    image = image.filter(ImageFilter.MedianFilter(size=3))
    
    image.save("processed_captcha.png")

    image.show()

    # Extract text
    #captcha_text = pytesseract.image_to_string(image, config="--psm 6").strip()
    captcha_text = pytesseract.image_to_string(Image.open("captcha.png"), config="--psm 6").strip()

    print(captcha_text)
    if captcha_text:
        print("Extracted CAPTCHA Text:", captcha_text)
    else:
        print("No text detected in CAPTCHA. Check the image quality.")

except Exception as e:
    print("Error during OCR processing:", e)
