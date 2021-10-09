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
        #Preconditions:   I log in with account "<account_name>" 
        username = 'pueihrdqcd'
        like_image =3
        email = username()
        pwd = password()
        url = 'https://unsplash.com/@' + username + '/' + 'likes'
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
        
        print("Get the init like imgae")
        self.browser.get(url)
        init_number_like = steps_profile(self.browser).get_number_like()
        # Go to home screen
        home_steps(self.browser).home_click()
        time.sleep(2)
        ###I like 3 random photos
        i =1
        print ('Like 3 random photo')
        while  i <= like_image: 
            home_steps(self.browser).hover_image(i)
            time.sleep(2)
            home_steps(self.browser).like_image(i)
            time.sleep(2)
            
            prod_cato = self.browser.find_element(By.XPATH, logo_home())
            actions = ActionChains(self.browser)
            actions.move_to_element(prod_cato).perform()
            i = i + 1
             
        #When I go to *https://unsplash.com/@user_name/likes* 
        
        self.browser.get(url)
        #Then I see the number of likes is 3 
        print("Get number like on profile screen")
        time.sleep(2)
        number_like = steps_profile(self.browser).get_number_like()
        compare_like_image = init_number_like + like_image
        print("Verify the number of like on Like section")
        self.assertEqual(number_like, compare_like_image, "The number of likes wrong!")
        
        ### And 3 photos appear in Likes section 
        count = steps_profile(self.browser).count_like_image()
        print("Verify the new like images appear in Likes section")
        self.assertEqual(compare_like_image, count, "New like images display wrong on Like section")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()