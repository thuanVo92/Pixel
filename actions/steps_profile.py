'''
Created on Oct 8, 2021

@author: DELL
'''
from selenium.webdriver.common.by import By
from pages.page_profile import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
import json

class steps_profile():
    '''
    classdocs
    '''
    def __init__(self,driver):
        self.driver = driver
        
    def edit_click(self):
        print("+++Click on Edit button")
        self.clickEditbutton()
    
    def edit_username(self, username):
        print("+++[Step] Edit user name")
        self.inputUserName(username)
        time.sleep(2)
        # self.clickUpdateLogin()
        
    def get_status_update_profile(self):
        print("+++Check update profile")
        delay = 1
        if WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, dialog_update_account_succ()))):  
            status = "Account updated!"         
        else:
            status = "Account failed!"
        print("+++Status:" + status)
        return status
        
    def get_fullname(self):
        print("Get full name")
        b= self.driver.find_element(By.XPATH, txt_fullname()).text
        print("+++The full name is", b)
        return b
    
    def get_number_like(self):
        print("Get number likes.")
        sb = self.driver.find_element(By.XPATH, like_number()).text
        number_like = [int(s) for s in sb.split() if s.isdigit()]
        print("+++The nummber likes on Like section is ", number_like[0])
        return number_like[0]
    
    def count_like_image(self):
        print("Count number likes.")
        count = self.driver.find_elements_by_class_name(frame_image())
        print("+++The nummber images on Like section is ", len(count))
        return (len(count))
        
        
    #get element
    def get_bntEdit(self):
        return self.driver.find_element(By.XPATH, btn_edit())

    def get_txtUsername(self):
        return self.driver.find_element(By.XPATH, txt_username())
    
    def get_bntUpdate(self):
        return self.driver.find_element(By.XPATH, btn_update())
    
    #Action
    def clickEditbutton(self):
        self.get_bntEdit().click()
    
    def inputUserName(self, username):
        print("[+] Input email")
        self.get_txtUsername().clear()
        self.get_txtUsername().send_keys(username)
    
    def clickUpdateLogin(self):
        self.get_bntUpdate().click()
        
