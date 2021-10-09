'''
Created on Oct 4, 2021

@author: DELL
'''
from selenium import webdriver
import time
import base64

def customChrome() :
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options= option, executable_path= "../drivers/chromedriver.exe")
    size = driver.get_window_size()
    print(size);
    driver.maximize_window();
    
    print ("[Open browser] Open google chrome browser");
    return driver;

def getDecodedpassword(password):
    return base64.b64encode("123456".encode("utf-8"))
