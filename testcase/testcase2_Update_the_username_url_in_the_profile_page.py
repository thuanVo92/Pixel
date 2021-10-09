'''
Created on Oct 8, 2021

@author: DELL
'''
import unittest

from utils.CustomChromeDriver import customChrome
from testdata.testdata import *
from actions.home_steps import home_steps
from actions.login_steps import stepLogin
from actions.steps_profile import steps_profile
from pages.page_home import *
from pages.page_login import *
from pages.page_profile import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
import json
import random  
import string 


class Testcase2(unittest.TestCase):
    

    def setUp(self):
        print ("==========[Begin Test]=====")
        self.browser = customChrome()
        self.browser.get("https://unsplash.com/")
        time.sleep(2)
        
        
    def testName(self):
        your_fullname = 'Thuan Vo'
        url = "https://unsplash.com"
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
        
        ###I go to the Profile page 
        home_steps(self.browser).icon_user_click()
        home_steps(self.browser).menu_view_profile_click()
        time.sleep(1)
        get_title1 = self.browser.title
        
        #When I click Edit tags link 
        steps_profile(self.browser).edit_click()
        
        ###  I edit the username field 
        status_update = 'Account failed!'
        while status_update != 'Account updated!':
            username_edit = Upper_Lower_string(10)
            print (username_edit)
            time.sleep(2)
            steps_profile(self.browser).edit_username(username_edit)
            time.sleep(2)
            steps_profile(self.browser).clickUpdateLogin()
            time.sleep(2)    
            status_update = steps_profile(self.browser).get_status_update_profile()
 
        ###I go to https://unsplash.com/@<new_username> 
        new_url = url + '\@' + username_edit
        
        self.browser.get(new_url)

        #Then I observe that it will take me to the Profile page 
        get_title2 = self.browser.title
        title_view_profile = your_fullname + ' (@' + username_edit + ') | Unsplash Photo Community'
        self.assertEqual(title_view_profile, get_title2, "Profile page is displayed.")
        ###And My full name is displayed as <your_fullname> 

        fullname = steps_profile(self.browser).get_fullname()
        print("Verify My full name is displayed as", your_fullname )
        self.assertEqual(fullname, your_fullname, "Wrong full name")
        ############
        
    def tearDown(self):
        self.browser.quit()
        print("==========[End Test]=========")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()