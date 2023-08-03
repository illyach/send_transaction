from selenium import webdriver
import os
import time


options = webdriver.ChromeOptions()

options.add_argument(r"--user-data-dir=/Users/illyach/Library/Application Support/Google/Chrome")


options.add_argument(r'--profile-directory=Profile 19') #e.g. Profile 3
driver = webdriver.Chrome(options=options)



time.sleep(1)
driver.get("https://www.google.com")

time.sleep(1)
driver.quit


