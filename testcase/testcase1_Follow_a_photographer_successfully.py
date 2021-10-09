'''
Created on Oct 7, 2021

@author: DELL
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time


from utils.CustomChromeDriver import customChrome
from testdata.testdata import *
from actions.home_steps import home_steps
from actions.login_steps import stepLogin
from actions.steps_images_detail import steps_image_detail
from pages.page_home import *
from pages.page_login import *
from pages.page_image_detail import *
from idlelib import tooltip


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print ("==========[Begin Test]=====")
        self.browser = customChrome()
        self.browser.get("https://unsplash.com")
        time.sleep(2)
    
  
    def test_case1(self): 
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
        
        ###I go to the home page. 
        home_steps(self.browser).home_click()
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, home_logo())))
            print ("Home page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
            
        ###I click the first photo on home page 
        home_steps(self.browser).first_image_click()
        time.sleep(2)
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, a())))
            print ("The first image is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
                       
        #Step: I hover on icon user at the top left corner and click the Follow button
        steps_image_detail(self.browser).follow_click()
        time.sleep(5)
        
        #Then I observe button background color turn into white and button text turn into Following 
        bckgclr = steps_image_detail(self.browser).get_color_follow_button()
        print("Verify Background of Following button")
        self.assertEqual("(255, 255, 255, 0)", bckgclr, "Background of Following button isn't white.")
        print("Verify text of Following button")
        tooltipText = steps_image_detail(self.browser).get_text_follow_button()
        self.assertEqual("Following", tooltipText, "Not found Following text")

    def tearDown(self):
        self.browser.quit()
        print("==========[End Test]=========")
        
if __name__=='__main__':
    unittest.main()