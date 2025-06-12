from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests 
from time import sleep

# WebDriver'ı başlat
driver = webdriver.Chrome()

sleep(5)

url='https://www.indeed.com'

driver.get=(url)

sleep(5)


# 1. Get the page

# search_input = driver.find_element_by_xpath('//*[@id="jobsearch"]/div/div[1]')
# search_input.send_keys('turkey')
# search_input.send_keys(Keys.RETURN)
# sleep(5)
