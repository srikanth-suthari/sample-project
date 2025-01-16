from selenium.webdriver.support.ui import Select
from selenium import webdriver
from PIL import Image
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image, ImageFilter
import pytesseract
import time         # brew install tesseract

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

driver = webdriver.Firefox()
driver.get('https://dharani.telangana.gov.in/knowLandStatus')

time.sleep(2)

# Locate CAPTCHA image element
captcha_element = driver.find_element(By.XPATH, "//form//section//div//div//div//div//div//div//img")
captcha_element.screenshot("/Users/srikanth/test-dir/captcha.png")

# Use Tesseract to extract text
captcha_text = pytesseract.image_to_string(Image.open("/Users/srikanth/test-dir/captcha.png")).strip()

# Print the CAPTCHA text
print(f"CAPTCHA text: {captcha_text}")

time.sleep(2)

# Fill CAPTCHA input
captcha_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Captcha']")
#print(captcha_input)
captcha_input.send_keys(captcha_text)
