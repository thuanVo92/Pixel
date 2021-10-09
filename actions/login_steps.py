'''
Created on Oct 5, 2021

@author: DELL
'''
from selenium.webdriver.common.by import By
from pages.page_login import *
from selenium import webdriver


class stepLogin:
    def __init__(self,driver):
        self.driver = driver
        
    def login(self, username, password):
        print("+++[Step] Login")
        self.inputUserName(username)
        self.inputPassword(password)
        self.clickButtonLogin()

        
    #Action
    def inputUserName(self, email):
        print("+++[+] Input email")
        self.get_txtUsername().send_keys(email)
        
    def inputPassword(self, password):
        print("+++[+] Input password")
        self.get_txtPassword().send_keys(password)
        
    def clickButtonLogin(self):
        print("+++[+] Click button Login")
        self.get_bntLogin().click()
        
        
    #get element
    def get_txtUsername(self):
        return self.driver.find_element(By.XPATH, txt_email())
    
    def get_txtPassword(self):
        return self.driver.find_element(By.XPATH, txt_password())
    
    def get_bntLogin(self):
        return self.driver.find_element(By.XPATH, btn_login())
    
    def get_Login_icon(self):
        return self.driver.find_element(By.XPATH, icon_login())
    