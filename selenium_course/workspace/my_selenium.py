from selenium  import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://www.google.com")  # open google.com
input= driver.find_element(By.NAME, "q")  # find input field

input.send_keys("feritya github")  # send keys to input field
sleep(2)  # wait 2 seconds
findClick=driver.find_element(By.NAME,"btnK")  # find search button
sleep(2)
findClick.click()  # click search button
sleep(2)
firstLink=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a")  # find first link//*[@id="rso"]/div[1]/div/div/div[1]/div/a
sleep(2)
firstLink.click()  # click first link
sleep(2)
firstList=driver.find_elements(By.CLASS_NAME,"core-section-container my-3 core-section-container--with-border border-b-1 border-solid border-color-border-faint m-0 py-3 pp-section languages")  # find all links for me in github
sleep(2)
print(f'benim linkedin hesabımda :{len(firstList)} tane önerilen faliyet bulunmaktadır')  # print number of links
while True:
    sleep(10)