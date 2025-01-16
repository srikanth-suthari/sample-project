from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome WebDriver
#driver_path = "path/to/chromedriver"  # Replace with your ChromeDriver path
driver = webdriver.Firefox()

try:
    # Open the webpage
    driver.get("https://dharani.telangana.gov.in/knowLandStatus")  # Replace with the Dharani portal or target website

    # Wait for the first dropdown to be present
    first_dropdown_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "districtID"))  # Replace with the actual ID
    )

    # Select an option from the first dropdown
    first_dropdown = Select(first_dropdown_element)
    first_dropdown.select_by_value("1")  # Replace with the desired option text
    print("Selected district option in the first dropdown.")

    # Wait for the second dropdown to be updated or enabled
    second_dropdown_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "mandalID"))  # Replace with the actual ID
    )

    # Select an option from the second dropdown
    second_dropdown = Select(second_dropdown_element)
    second_dropdown.select_by_value("4")  # Replace with the desired option text
    print("Selected mandal option in the second dropdown.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
