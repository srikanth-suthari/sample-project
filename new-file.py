from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/usr/local/bin/chromedriver')

# this is for a service
driver = webdriver.Chrome()

dropdown = driver.find_element(by=By.ID, value="districtID")
