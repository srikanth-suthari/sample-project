import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumbase import BaseCase


# Define the URL
url = "https://dharani.telangana.gov.in/knowLandStatus"

# Open the URL in the default web browser
webbrowser.open(url)



class DharaniTest(BaseCase):
    def test_dharani_page(self):
        url = "https://dharani.telangana.gov.in/knowLandStatus"

# Open the URL in the default web browser
        webbrowser.open(url)

        # open web page
        #self.open("https://dharani.telangana.gov.in/knowLandStatus")

        # entering values in the fields
        self.send_keys(".districtID input", "Medak")
        self.send_keys(".mandalID input", "Narsingi")
        self.send_keys(".vilageId input", "Narsingi")
        self.send_keys(".surveyIdselect input", "4")
        self.send_keys(".khataNoIdselect input", "153")

        # for clicking fetch button
        self.click("Fetch")

        # response from site
        # self.assert_text("successfully got responese from site")
        print("successfully got responese from site")
        