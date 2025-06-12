from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium import webdriver

sleep(1)

driver = webdriver.Chrome(executable_path=r'D:\download\chrome driver\chrome-win64\chromedriver.exe')
sleep(1)
url ="https://www.indeed.com/"
job = driver.find_element_by_xpath('//*[@id="mosaic-provider-jobcards"]/ul/li[1]')
driver.get(url)
sleep(5)
