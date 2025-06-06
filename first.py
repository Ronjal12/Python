from selenium import webdriver
import time
browser=webdriver.Chrome('chromedriver.exe')
browser.get('https://instagram.com/')
time.sleep(4)

#Automating the login
def login():
    username=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input')
    username.send_keys('Username')
    time.sleep(4)
    password=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input')
    password.send_keys('password')
    password.submit()
    time.sleep(6)
    login()