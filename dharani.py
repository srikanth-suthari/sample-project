from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For listing and selecting district
def test_district():
    # select the browser
    driver = webdriver.Firefox()
    driver.get("https://dharani.telangana.gov.in/knowLandStatus")
    # selecting district with xpath
    District_select = Select(driver.find_element(By.XPATH, ("//body/form/section/div/div/div/div/div/div[1]/select[1]")))

    # Find the options present in the dropdown 
    options = District_select.options
    # to print no.of districts
    print(f"Total options in the district dropdown are: {len(options)}")

    # selecting district in these 3 types
    #District_select.select_by_index(1) # option 1
    #District_select.select_by_value("16") # option 2
    District_select.select_by_visible_text("Nagarkurnool|నాగర్ కర్నూల్") # option 3
