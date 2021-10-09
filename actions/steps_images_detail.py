'''
Created on Oct 7, 2021

@author: DELL
'''
from selenium.webdriver.common.by import By
from pages.page_image_detail import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from idlelib import tooltip

from pages.page_image_detail import *
from pages.page_profile import txt_fullname

class steps_image_detail():
    '''
    classdocs
    '''


    def __init__(self,driver):
        self.driver = driver
    
    
    def follow_click(self):
        print("+++Click Follow  image")
        #mouse hover over
        prod_cato = self.driver.find_element(By.XPATH, icon_user())
        actions = ActionChains(self.driver)
        actions.move_to_element(prod_cato).perform()
        time.sleep(3)
        
        #click on follow button from dropdown
        ipads = self.driver.find_element(By.CSS_SELECTOR, btn_follow())
        actions.move_to_element(ipads).click().perform()
        
        time.sleep(2)
        msg = self.driver.find_element(By.XPATH, msg_follow())
        msg.click()
    
    def btn_download_click(self):
        print("+++Click on Download button")
        i= self.driver.find_element(By.XPATH, btn_download())
        i.click()
        time.sleep(20)
    
    def get_color_follow_button(self):
        #mouse hover over
        prod_cato = self.driver.find_element(By.XPATH, icon_user())
        actions = ActionChains(self.driver)
        actions.move_to_element(prod_cato).perform()
        time.sleep(3)
        bckgclr = self.driver.find_element(By.CSS_SELECTOR, btn_following()).value_of_css_property("background-color")
        return bckgclr
    
    def get_text_follow_button(self):
        #mouse hover over
        prod_cato = self.driver.find_element(By.XPATH, icon_user())
        actions = ActionChains(self.driver)
        actions.move_to_element(prod_cato).perform()
        time.sleep(3)

        toolTip = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, btn_following())))
        hov = ActionChains(self.driver).move_to_element(toolTip)
        txt = hov.perform()
        tooltipText = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Following'[class='ONxrv'"))).text
        print(tooltipText)
        return tooltipText
    
    def define_image_download_name(self):
        get_title1 = self.driver.current_url
        x = get_title1.split("https://unsplash.com/photos/")
        b1=x[1]
        b= self.driver.find_element(By.XPATH, name_owner()).text
        c = b+"-" + b1+"-unsplash"
        return c
    
    def get_image_download_name(self):
        print("+++Get the info of the download image from Windown")
        d = "unsplash"
        return d
    

    #Action      
    
        
    #get element
    def get_iconuser(self):
        return self.driver.find_element(By.XPATH, icon_user())
        
    def get_btnFollow(self):
        return self.driver.find_element(By.XPATH, btn_follow())
        