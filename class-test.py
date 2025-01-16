from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dharani:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://dharani.telangana.gov.in/knowLandStatus")
        
    def select_district(self, Select):
        district_select = Select(self.driver.find_elements(By.NAME, "districtID") [0] )
        district_select.select_by_value("6")
        
    def select_mandal(self, Select):
        mandal_select = Select(self.driver.find_elements(By.NAME, "mandalID"))
        #mandal_select.select_by_value(mandal)
        mandal_select.select_by_value("1")
        
    def close(self):
        self.driver.quit()
