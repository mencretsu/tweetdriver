from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
  
#input ur username/mail and password bellow
username = 'bejembut_name'
password = 'berjembut_pass'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://twitter.com/login")

sleep(10) #change this according to your load driver speed
userinput = driver.find_element(By.NAME, "text")
userinput.send_keys(username)
userinput.send_keys(Keys.ENTER)
print("email submitted")

sleep(2)
passinput= driver.find_element(By.NAME, "password")
passinput.send_keys(password)
passinput.send_keys(Keys.ENTER)
print("password submitted\nsuccess login")