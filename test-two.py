from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up the WebDriver (e.g., Chrome)
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")  # Update with the correct path

driver = webdriver.Chrome()

url = "https://dharani.telangana.gov.in/knowLandStatus"  # Replace with the actual URL of the form
driver.get(url)


try:
    # Navigate to the Dharani portal
    driver.get("https://dharani.telangana.gov.in/knowLandStatus")

    # Wait for the page to load and the search form to be visible
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "landSearchButton"))  # Replace with the actual element's ID or XPath
    )

    # Example: Click on "Land Details Search" (replace with the actual ID or XPath)
    land_search_button = driver.find_element(By.ID, "landSearchButton")
    land_search_button.click()

    # Wait for the next page or form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "surveyNumberInput"))  # Replace with the actual element's ID
    )

    # Fill in the details (e.g., district, mandal, village, survey number)
    district_dropdown = driver.find_element(By.ID, "districtID")  # Replace with the actual ID
    district_dropdown.click()
    district_option = driver.find_element(By.XPATH, "//option[@value='Medak']")  # Replace with the desired district
    district_option.click()

    mandal_dropdown = driver.find_element(By.ID, "mandalID")  # Replace with the actual ID
    mandal_dropdown.click()
    mandal_option = driver.find_element(By.XPATH, "//option[@value='Narsingi']")  # Replace with the desired mandal
    mandal_option.click()

    village_dropdown = driver.find_element(By.ID, "villageId")  # Replace with the actual ID
    village_dropdown.click()
    village_option = driver.find_element(By.XPATH, "//option[@value='Narsingi']")  # Replace with the desired village
    village_option.click()

    survey_input = driver.find_element(By.ID, "4")  # Replace with the actual ID
    survey_input.send_keys("153")  # Replace with the desired survey number

    # Submit the form
    submit_button = driver.find_element(By.ID, "Fetch")  # Replace with the actual ID
    submit_button.click()

    # Wait for results to load and print them
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "resultTable"))  # Replace with the actual class or ID of the results
    )
    results = driver.find_element(By.CLASS_NAME, "resultTable").text
    print(results)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()