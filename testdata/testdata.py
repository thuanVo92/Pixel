'''
Created on Oct 9, 2021

@author: DELL
'''
import random  
import string  


def Upper_Lower_string(length): # define the function and pass the length as argument  
    # Print the string in Lowercase  
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length))) # run loop until the define length  
    return result

def username():
    return 'thithuan.it92@gmail.com'

def password():
    return '123456'