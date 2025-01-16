from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


# Initialize the WebDriver (Make sure to specify the path if not in PATH)
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

# Open the desired URL
url = "https://dharani.telangana.gov.in/knowLandStatus"  # Replace with the actual URL of the form
driver.get(url)

# Optional: Maximize the window for better visibility
driver.maximize_window()

time.sleep(30)


# Wait for the page to load completely  # You can use WebDriverWait for a more robust solution

# Fill in the form fields (replace 'field_id' with actual IDs or use other locators)

dropdown_element_1 = driver.find_element(By.ID, "districtID", input("enter district name: "))  # for district
select = Select(dropdown_element_1)  # for distict
dropdown_element_2 = driver.find_element(By.ID, "mandalID", input("enter mandal name: "))    # for mandal
select = Select(dropdown_element_2)
dropdown_element_3 = driver.find_element(By.ID, "villageId")  # for village
select = Select(dropdown_element_3)
# driver.find_element(By.ID, "surveyIdselect").send_keys(int(4))  # for survey number
# driver.find_element(By.ID, "khataNoIdselect").send_keys(int(153)) # for khata number
# select = Select(dropdown_element_1)
# select = Select(dropdown_element_2)
# select = Select(dropdown_element_3)

#select.select_by_visible_text("Medak").lower()
#select.select_by_visible_text("Narsingi").lower()
#select.select_by_visible_text("Narsingi").lower()

# Click the submit button
# driver.find_element(By.ID, "Fetch").click()  # Replace with actual submit button ID

# Optional: Wait for a success message or any other indication
# Adjust as necessary