'''
Created on Oct 4, 2021

@author: DELL
'''
def btn_login():
    return "//a[contains(text(),'Log in')]"

def logo_home():
    return "//header/nav[1]/a[1]/*[1]"

def location_image(i):
    if i ==1:
        res = "//body/div[@id='app']/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/figure[1]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]/img[1]"
    if i ==2:
        res = "//body/div[@id='app']/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[2]/figure[1]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]/img[1]"
    if i ==3:
        res = "//body/div[@id='app']/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[3]/figure[1]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]/img[1]"
    return res   
          
def home_logo():
    return "//body/div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]"

def icon_user():
    return "//header/nav[1]/div[6]/button[1]/div[1]/div[1]/img[1]"

def menu_view_profile():
    return "//a[contains(text(),'View profile')]"

def btn_like(i):
    if i==1:
        re = "//body/div[@id='app']/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/figure[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]"
    if i ==2:
        re = "//body/div[@id='app']/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[2]/figure[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]"
    if i ==3:
        re = "//body/div[@id='app']/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[3]/figure[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]"    
    return re