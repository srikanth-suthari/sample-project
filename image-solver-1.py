from selenium.webdriver.support.ui import Select
from selenium import webdriver
from PIL import Image
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
import data

url = "https://dharani.telangana.gov.in/knowLandStatus"
driver = webdriver.Firefox()
driver.get(url)

