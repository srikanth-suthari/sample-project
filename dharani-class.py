from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the webpage
driver.get("https://dharani.telangana.gov.in/knowLandStatus")

# Locate dropdown elements (e.g., by their IDs)
dropdown_ids = ["//body/form/section/div/div/div/div/div/div[1]/select[1]", # District
                "//body/form/section/div/div/div/div/div/div[2]/select[1]"] # Mandal

# Loop through each dropdown and select options
for dropdown_id in dropdown_ids:
    dropdown = Select(driver.find_element(By.XPATH, dropdown_id))
    dropdown.select_by_visible_text("Medak|మెదక్")  # Use visible text or value
    # dropdown.select_by_value("option_value")  # Or select by value
    # dropdown.select_by_index(1)  # Or select by index
    for j in dropdown_ids:    
        dropdown = Select(driver.find_element(By.XPATH, dropdown_id))
        dropdown.select_by_visible_text("Narsingi|నర్సింగి")

# Close the browser
