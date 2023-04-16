from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 

from selenium.webdriver.common.action_chains import ActionChains


class TestSouce():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def test_invalid_login(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "user-name")))
        username=self.driver.find_element(By.ID, "user-name")
        password=self.driver.find_element(By.ID,"password")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)

        
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn.click()
        sleep(5)
        while True:
           sleep(20)
           break


test = TestSouce()
test.test_invalid_login()