'''
Created on Oct 7, 2021

@author: DELL
'''
from selenium.webdriver.common.by import By
from pages.page_home import *
from test.test_fileinput import BaseFileInputGlobalMethodsTest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class home_steps():
    '''
    classdocs
    '''
    def __init__(self,driver):
        self.driver = driver
        
   
    def login_click(self):
        print("+++Click on Login button")
        self.clickLoginbutton()
    
    def home_click(self):
        print("+++Click on Home button")
        self.clickHomebutton()

    def first_image_click(self):
        print("+++Click on the first image on Home page")
        self.click_first_image()

    def icon_user_click(self):
        print("+++Click on icon user")
        self.click_icon_user()
    
    def menu_view_profile_click(self):
        print("+++Click on menu View Profile")
        self.click_menu_view_profile()
        
    def like_image(self, image):   
        print("+++Like a photo")
        self.click_like_button(image)
    
    def hover_image(self, image):
        print("+++Hover image", image)
        #mouse hover over
        prod_cato = self.driver.find_element(By.XPATH, location_image(image))
        actions = ActionChains(self.driver)
        actions.move_to_element(prod_cato).perform()
        time.sleep(3)
        
    #get element
    def get_bntLogin(self):
        return self.driver.find_element(By.XPATH, btn_login())
    
    def get_logoHome(self):
        return self.driver.find_element(By.XPATH, logo_home())
    
    def get_first_image(self):
        return self.driver.find_element(By.XPATH, location_image(1))
    
    def get_icon_user(self):
        return self.driver.find_element(By.XPATH, icon_user())
    
    def get_menu_view_profile(self):
        return self.driver.find_element(By.XPATH, menu_view_profile())
    

        
    
    #Action
    def clickLoginbutton(self):
        self.get_bntLogin().click()
    
    def clickHomebutton(self):
        self.get_logoHome().click()
        
    def click_first_image(self):
        self.get_first_image().click()
        
    def click_icon_user(self):
        self.get_icon_user().click()
        
    def click_menu_view_profile(self):
        self.get_menu_view_profile().click()
        
    def click_like_button(self,image):
        self.driver.find_element(By.XPATH, btn_like(image)).click()