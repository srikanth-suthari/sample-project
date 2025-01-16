from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()  # or use any browser of your choice
driver.get("https://dharani.telangana.gov.in/knowLandStatus")  # Replace with the URL containing your dropdown

# Locate the dropdown element
dropdown = driver.find_element(By.XPATH, "//body/form/section/div/div/div/div/div/div[1]/select[1]")  # Replace 'dropdown_id' with the actual ID of your dropdown

# Create a Select object
select = Select(dropdown)

# Select an option by visible text, value, or index
select.select_by_visible_text("Medak|మెదక్")  # Replace with the actual option text
# Alternatively: select.select_by_value("value_of_option")
# Alternatively: select.select_by_index(index_of_option)

# Give some time to see the result
time.sleep(0.5)

# for mandals
dropdown = driver.find_element(By.XPATH, "//body/form/section/div/div/div/div/div/div[2]/select[1]")
select = Select(dropdown)
select.select_by_visible_text("Narsingi|నర్సింగి")

time.sleep(0.5)

# for villages
dropdown = driver.find_element(By.XPATH, "//form//div[3]//select[1]")
select = Select(dropdown)
select.select_by_visible_text("Narsingi|నార్సింగ్")

time.sleep(1)

dropdown = driver.find_element(By.XPATH, "//body//form//div//div//div[1]//div[1]//select[1]")
select = Select(dropdown)
#select.select_by_value("1/అ") # with value
select.select_by_index(1) # with index
time.sleep(15)