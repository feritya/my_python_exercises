from selenium  import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://www.google.com")  # open google.com
input_field = driver.find_element(By.NAME, "q")  # find input field
print(f"girdi:{input_field}") 

while True:
    continue

