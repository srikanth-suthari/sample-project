from PIL import Image
import pytesseract

# Specify the path to the Tesseract binary
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Open the CAPTCHA image
image = Image.open("/Users/srikanth/test-dir/captcha.png")

#image.show()

# Extract text from the image
captcha_text = pytesseract.image_to_string(image, config="--psm 8").strip()
print("Extracted CAPTCHA Text:", captcha_text)

print(f"Raw OCR Output: '{captcha_text}'")