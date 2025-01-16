from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome WebDriver
driver_path = "path/to/chromedriver"  # Update with your ChromeDriver path
driver = webdriver.Firefox()

try:
    # Open the webpage
    driver.get("https://dharani.telangana.gov.in/knowLandStatus")  # Replace with the Dharani portal URL or target website

    # Wait for the dropdown to load
    dropdown_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "districeID" [0]))  # Replace with the actual ID of the dropdown
    )
    # Create a Select object
    dropdown = Select(dropdown_element)

    # Iterate through all options in the dropdown
    for index, option in enumerate(dropdown.options):
        # Select the option
        dropdown.select_by_index(index)
        print(f"Selected option: {option.text}")

        # Perform some action after selecting the option
        # Example: Click a button or wait for a result
        #next_button = driver.find_element(By.ID, "nextButtonID")  # Replace with the actual button ID
        #next_button.click()

        # Optionally wait for the next dropdown or process
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mandalID"[0]))  # Replace with relevant element ID
        )

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
