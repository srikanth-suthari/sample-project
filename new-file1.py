from selenium.webdriver.support.ui import Select
from selenium import webdriver
from PIL import Image
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
import time

def test_district():
    driver = webdriver.Firefox()
    #driver.maximize_window()
    driver.get("https://dharani.telangana.gov.in/knowLandStatus")

    # for districts
    #District_select = Select(driver.find_elements("id", "districtID")[0]) # working test
    District_select = Select(driver.find_element(By.XPATH, ("//body/form/section/div/div/div/div/div/div[1]/select[1]"))) # working test
    
    # Find the options present in the dropdown 
    #options = District_select.options

    #print(f"Total options in the district dropdown are: {len(options_1)}")
    #print()
    # printing the district options
    #for option in options:
    #    print(option.text)

    #District_select.select_by_index(1)
    #District_select.select_by_value("16")
    District_select.select_by_visible_text("Medak|మెదక్") # working test

    time.sleep(0.5)

    # for mandals
    Mandal_select = Select(driver.find_element(By.XPATH, ("//body/form/section/div/div/div/div/div/div[2]/select[1]")))
    #options = Mandal_select.options
    Mandal_select.select_by_visible_text("Narsingi|నర్సింగి")
    #print(f"Total options in the mandal dropdown are: {len(options_2)}")
    #print()

#def test_mandal():
    #Mandal_select = Select(WebDriverWait.until("id", "mandalID")[0])
    #Mandal_select.select_by_index("1")
    #Mandal_select = Select(driver.find_elements(By.XPATH, "//*[@id='mandalID']")[0])
    
    #print(Mandal_select.options)
    #Mandal_select.select_by_visible_text(input("Enter: ")) # working test
    
    # selecting mandal
    #mandal_select.select_by_value("463") # working test

    #print("Selected option " + select.first_selected_option.text)
    #assert "Medak" in select.first_selected_option.text
    #print("Selected option " + select.first_selected_option.text)
    
#test_district()
#test_mandal()
    time.sleep(0.5)

    # for villages
    dropdown = driver.find_element(By.XPATH, "//form//div[3]//select[1]")
    select = Select(dropdown)
    select.select_by_visible_text("Narsingi|నార్సింగ్")
    time.sleep(1)

    # for survey numbers
    dropdown = driver.find_element(By.XPATH, "//body//form//div//div//div[1]//div[1]//select[1]")
    select = Select(dropdown)
    select.select_by_value("1/అ")
    time.sleep(0.5)

    dropdown = driver.find_element(By.XPATH, "//body//form//div//div//div//div//div[2]//div[1]//select[1]")
    select = Select(dropdown)
    select.select_by_index(1)
    time.sleep(15)

    captcha_element = driver.find_element(By.XPATH, "//form//section//div//div//div//div//div//div//img[@alt='captcha']")
    captcha_element.screenshot("/Users/srikanth/test-dir/captcha.png")

    # Use Tesseract to extract text
    captcha_text = pytesseract.image_to_string(Image.open("captcha.png")).strip()
    print(f"CAPTCHA text: {captcha_text}")