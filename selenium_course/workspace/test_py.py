from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date
import pytest

class  Test_Demmo:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.today = str(date.today())
        Path = (self.folderPath).mkdir( exist_ok=True) 
    def teardown_method(self):
        self.driver.quit()    
    
    @pytest.mark.parametrize("username,password",[])
    def test_invalid_login(self,username,password):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        WepDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys("username")
        passwordInput.send_keys("password")

        LoginBtn=self.driver.find_element(By.ID,"login-button")
        LoginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
    def test_func_demo(self):
            a=1
            if a==1:
                assert True

