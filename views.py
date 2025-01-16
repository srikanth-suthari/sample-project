# views.py
from django.shortcuts import render
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def web_automation(request):
    if request.method == "POST":
        # Get data from the form
        search_term = request.POST.get("search_term")
        dropdown_option = request.POST.get("dropdown_option")
        
        # Run Selenium automation based on the input
        result = run_selenium_script(search_term, dropdown_option)
        
        # Return the result as JSON or render a success page
        return JsonResponse({"status": "success", "result": result})
    
    # Render the form template for GET requests
    return render(request, "web_automation.html")

def run_selenium_script(search_term, dropdown_option):
    # Set up Selenium WebDriver
    driver = webdriver.Chrome()  # Or any other WebDriver like Firefox
    driver.implicitly_wait(10)

    try:
        if dropdown_option == "google":
            driver.get("https://www.google.com")
            search_box = driver.find_element(By.NAME, "q")
        elif dropdown_option == "bing":
            driver.get("https://www.bing.com")
            search_box = driver.find_element(By.NAME, "q")
        
        # Perform the search
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(2)  # Wait for results to load

        # Extract some results (e.g., titles of search results)
        results = driver.find_elements(By.CSS_SELECTOR, "h3")[:5]
        titles = [result.text for result in results]
        return titles

    finally:
        driver.quit()
