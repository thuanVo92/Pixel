'''
Created on Oct 8, 2021

@author: DELL
'''
import unittest

from selenium.webdriver.support.ui import WebDriverWait
from testdata.testdata import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
import json

from utils.CustomChromeDriver import customChrome
from actions.home_steps import *
from actions.login_steps import *
from actions.steps_images_detail import *
from pages.page_home import *
from pages.page_login import *
from pages.page_image_detail import *

class Test(unittest.TestCase):


    def setUp(self):
        print ("==========[Begin Test]=====")
        self.browser = customChrome()
        self.browser.get("https://unsplash.com/")
        time.sleep(2)


    def tearDown(self):
        self.browser.quit()
        print("==========[End Test]=========")


    def testcase5(self):
        email = username()
        pwd = password()
        #Preconditions:   I log in with account "<account_name>" 
        print ("Click on Login button")
        home_steps(self.browser).login_click()
        delay = 3
        try:           
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, icon_login())))
            print ("Login page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        
        print("Input user & pass to login")
        stepLogin(self.browser).login(email, pwd)
        # When I open a random photo 
        ###I click the first photo on home page 
        home_steps(self.browser).first_image_click()
        time.sleep(2)
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, a())))
            print ("The first image is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
        # And I download this photo 
        time.sleep(1)
        steps_image_detail(self.browser).btn_download_click()
        
        #Then I notice that the image is downloadable and the correct image has been saved 
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, dialog_thank())))
            print ("Thank you dialog is displayed!")
        except TimeoutException:
            print ("The image isn't download")
        
        image_download_name = steps_image_detail(self.browser).define_image_download_name()
        image_download_name_windown = steps_image_detail(self.browser).get_image_download_name()
        self.assertEqual(image_download_name, image_download_name_windown, "The download image wrong name.")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()