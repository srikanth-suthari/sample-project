from seleniumbase import BaseCase
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class DharaniTest(BaseCase):

    def open_url_with_webbrowser(url):
        try:
            webbrowser.open(url)
            print(f"Opened {url} in the default web browser.")
        except Exception as e:
            print(f"Error opening URL: {e}")

    open_url_with_webbrowser("https://www.google.com")
        
    def test_dharani_page(self):



            # webbrowser.open("https://dharani.telangana.gov.in/knowLandStatus")

            # open web page
        # self.open("https://dharani.telangana.gov.in/knowLandStatus")

        self.open("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_text")

        #self.send_keys("fname input", "srikanth")
        # self.send_keys("lname input", "kumar")

        # self.click("submit")

            # entering values in the fields
        #self.send_keys(".districtID input", input("enter district name: "))
        #self.send_keys(".mandalID input", "Narsingi")
        #self.send_keys(".vilageId input", "Narsingi")
        #self.send_keys(".surveyIdselect input", "4")
        #self.send_keys(".khataNoIdselect input", "153")

            # for clicking fetch button
        # self.click("Fetch")

            # response from site
            # self.assert_text("successfully got responese from site")
print("successfully got responese from site")