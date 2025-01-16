from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def test_district():
    driver = webdriver.Firefox()
    #driver.maximize_window()
    driver.get("http://prereg.telangana.gov.in/AgricultureEC/index.htm")

    # Document Number
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                "//div//div//div//div//div[1]//input[1]"))
                ).send_keys(input("Enter Document Number: "))
    time.sleep(0.5)

    # Year of Registration
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                "//body/div/div/div/form[@action='Search_Document_Details.htm']/div/div[2]/input[1]"))
                ).send_keys(input("Enter Year of Registration: "))
    time.sleep(0.5)

    # Registered at SRO
    SRO = input("Enter SRO: ")
    if SRO == "ramayampet".lower():
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                    "//input[@value='()']"))
                    ).clear()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                    "//input[@value='()']"))
                    ).send_keys(SRO.upper())
    time.sleep(0.5)

    # Submit button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                "//button[@type='submit']"))
                ).click()
    time.sleep(2)

    # GetEC button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                "//form[@action='EC_Report.htm']//button[@type='submit']"))
                ).click()
    time.sleep(1)

    # For Printing the Actual Document from the portal
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                "//button[@type='button']"))
                ).click()
    time.sleep(1)