from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class   Test_Demmo:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
    def teardown_method(self):
        self.driver.quit()    
    def test_func_demo(self):
        a ="hello"
      
    def test_invalid_login(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        WepDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        
        LoginBtn=self.driver.find_element(By.ID,"login-button")
        LoginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"


