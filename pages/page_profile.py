'''
Created on Oct 8, 2021

@author: DELL
'''
def btn_edit():
    return ("//body/div[@id='app']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]")

def txt_username():
    return ("//input[@id='user_username']")

def btn_update():
    return ("//body/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[6]/div[1]/div[1]/input[1]")

def txt_fullname():
    return ("//div[contains(text(),'Thuan Vo')]")

def dialog_update_account_succ():
    return ("//div[contains(text(),'Account updated!')]")

def dialog_update_account_fail():
    return ("//body/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]")

def like_number():
    return ("//body/div[@id='app']/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]")

def frame_image():
    return "oCCRx"