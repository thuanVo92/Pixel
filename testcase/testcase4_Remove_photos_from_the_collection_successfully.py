'''
Created on Oct 8, 2021

@author: DELL
'''
import unittest

from utils.CustomChromeDriver import customChrome
from testdata.testdata import *
from actions.home_steps import home_steps
from actions.login_steps import stepLogin
from actions.steps_profile import *
from pages.page_home import *
from pages.page_login import *
from pages.page_profile import *
from verify.verify_profile import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import time

class Test(unittest.TestCase):


    def setUp(self):
        print ("==========[Begin Test]=====")
        self.browser = customChrome()
        self.browser.get("https://unsplash.com/")
        time.sleep(2)


    def tearDown(self):
        self.browser.quit()
        print("==========[End Test]=========")


    def testName(self):
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
        # And I create a private collection 
        # And I add 2 random photos to the newly created collection 
        # And I remove 1 photo from the newly created collection 
        # When I go to *https://unsplash.com/collections/collection_id* 
        # Then I notice that the photo has been removed successfully from the collection 
        # And there is only 1 remaining photo in the collection 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()