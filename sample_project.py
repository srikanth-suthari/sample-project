from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Initialize WebDriver (here using Chrome)
driver = webdriver.Chrome(executable_path="path_to_chromedriver")  # Specify path to your ChromeDriver

# Open the website with the form
url = "https://example.com/form"  # Replace with the URL of the form you want to automate
driver.get(url)

# Maximize the window (optional)
driver.maximize_window()

# Locate the fields by their name, id, or other attributes
# Replace the element identifiers with the actual ones used by the form

# Example 1: Filling out a text field
name_field = driver.find_element(By.ID, "name")  # Replace 'name' with the actual field ID or other locator
name_field.send_keys("John Doe")  # Replace with the text you want to enter

# Example 2: Selecting an option from a dropdown (if applicable)
dropdown = driver.find_element(By.ID, "dropdown")  # Replace 'dropdown' with actual dropdown field ID
dropdown.click()
dropdown_option = driver.find_element(By.XPATH, "//option[text()='Option 2']")  # Replace with the correct option text or XPath
dropdown_option.click()

# Example 3: Filling out a date field
date_field = driver.find_element(By.ID, "date")  # Replace with the actual field ID for date
date_field.send_keys("01/01/2025")  # Enter a date

# Example 4: Checking a checkbox
checkbox = driver.find_element(By.ID, "accept_terms")  # Replace with actual checkbox field ID
if not checkbox.is_selected():
    checkbox.click()

# Example 5: Clicking a submit button
submit_button = driver.find_element(By.ID, "submit_button")  # Replace with the actual ID of the submit button
submit_button.click()  # Click the submit button to submit the form

# Optionally, wait for the next page or confirmation (e.g., after form submission)
driver.implicitly_wait(5)  # Wait for 5 seconds (adjust as needed)

# Close the browser after the operation is complete
driver.quit()
