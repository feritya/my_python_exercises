from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ac 
#action chaines
from selenium.webdriver.common.action_chains import ActionChains


class TestSel:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    






    def invalid_test(self):

        WebDriverWait(self.driver , 10).until(ac.visibility_of_element_located((By.ID, "user-name")))    
        username=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver, 5).until(ac.visibility_of_element_located((By.ID, "password")))
        password=self.driver.find_element(By.ID,"password")
        
        username.send_keys("1")
        password.send_keys("1")
        login=self.driver.find_element(By.ID,"login-button")
        login.click()
        

        error_message=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        teterror=error_message.text == "Epic sadface: Username and password do not match any user in this service"
    
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 10).until(ac.visibility_of_element_located((By.ID, "user-name")))
        username=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver, 5).until(ac.visibility_of_element_located((By.ID, "password")))
        password=self.driver.find_element(By.ID,"password")
        action = ActionChains(self.driver)
        action.send_keys_to_element(username, "standard_user")
        action.send_keys_to_element(password,"secret_sauce")
        action.perform()
        login=self.driver.find_element(By.ID,"login-button")
        login.click()
        sleep(2)
        
        
        
        
        
        while True:
            continue

        
        


test=TestSel()
test.invalid_test()
test.test_valid_login()
