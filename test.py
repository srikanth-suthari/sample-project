print("PQPI")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

# Path to your ChromeDriver
driver_path = "/opt/homebrew/bin/chromedriver"  # Update with your correct path

# Use the Service class to specify the ChromeDriver path
service = Service(driver_path)


# Pass the Service object when initializing the WebDriver
driver = webdriver.Chrome(service=service)


# Wait for the page to load
time.sleep(5)  # Adjust as necessary for slower or faster loading

# Locate the form fields for District, Mandal, and Village
# Example: Use the actual element IDs, names, or XPath from the page source

# Locate and select the District
district_element = driver.find_element(By.ID, "districtElementId")  # Replace with actual ID or name
district_element.send_keys("medak")  # Replace with desired district

# Locate and select the Mandal
mandal_element = driver.find_element(By.ID, "mandalElementId")  # Replace with actual ID or name
mandal_element.send_keys("Narsingi")  # Replace with desired mandal

# Locate and select the Village
village_element = driver.find_element(By.ID, "villageElementId")  # Replace with actual ID or name
village_element.send_keys("Narsingi")  # Replace with desired village

# Submit the form if necessary (example using a button click)
submit_button = driver.find_element(By.ID, "submitButtonId")  # Replace with actual submit button ID
submit_button.click()

# Wait for the page to process the form
time.sleep(5)

# Optionally, you can close the browser after completing the action
driver.quit()