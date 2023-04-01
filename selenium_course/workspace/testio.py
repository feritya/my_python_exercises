from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class LoginTest:
    def login_test(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        username=driver.find_element(By.ID,"user-name")
        password=driver.find_element(By.ID,"password")
        login_click =driver.find_element(By.ID,"login-button")
        sleep(2
        )
        username.send_keys("standard_user")
        password.send_keys("secret_saucewrong")
        sleep(1)
        login_click.click()
        sleep(1)
        error_message=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        teterror=error_message.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"error message is : {teterror}")
        sleep(2)
        while True:
            continue

    def blank_field(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        username=driver.find_element(By.ID,"user-name")
        password=driver.find_element(By.ID,"password")
        login_click =driver.find_element(By.ID,"login-button")
        sleep(2)
        username.send_keys("")
        password.send_keys("")
        sleep(1)
        login_click.click()
        sleep(1)
        error_message=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        if error_message.text == "Epic sadface: Username is required":
            print("error message is : True")
        elif error_message.text == "Epic sadface: Password  is required":
            print("error message is : True")
        else:
            print("error message is : False")
        while True:
            continue

    def locked_user(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        username=driver.find_element(By.ID,"user-name")
        password=driver.find_element(By.ID,"password")
        login_click =driver.find_element(By.ID,"login-button")
        sleep(2)
        username.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        sleep(1)
        login_click.click()
        sleep(1)
        error_message=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        if error_message.text == "Epic sadface: Sorry, this user has been locked out.":
            print("error message is : True")
        else:
            print("error message is : False")
        while True:
            continue

    def xbutton(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        username=driver.find_element(By.ID,"user-name")
        password=driver.find_element(By.ID,"password")
        login_click =driver.find_element(By.ID,"login-button")
        sleep(2)
        username.send_keys("")
        password.send_keys("")
        sleep(1)
        login_click.click()
        sleep(3)

        username_x=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/svg/path")
        password_x=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/svg/path")
        sleep(1)
     
        if username_x is not None and password_x is not None:
            print("x button is present")
        else:
            print("x button is not present")
        username_x.click()
        password_x.click()
        username_x=driver.find_element(By.XPATH,"//*[@id=2login_button_container'']/div/form/div[1]/svg/path")
        password_x=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[2]/svg/path")
        if username_x is None or password_x is None:
            print("x button is not working")
        else:
            print("x button is working")
        while True:
            continue
    def success_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)

        username=driver.find_element(By.ID,"user-name")
        password=driver.find_element(By.ID,"password")
        login_click =driver.find_element(By.ID,"login-button")
        sleep(1)
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        sleep(1)
        login_click.click()
        sleep(1)
        if driver.current_url=="https://www.saucedemo.com/inventory.html":
            print("login success")
        else:
            print("login failed")
        while True:
            continue
    def success_product(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)

        username=driver.find_element(By.ID,"user-name")
        password=driver.find_element(By.ID,"password")
        login_click =driver.find_element(By.ID,"login-button")
        sleep(1)
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        sleep(1)
        login_click.click()
        sleep(1)
        find_six_element=driver.find_elements(By.CLASS_NAME,"inventory_item")
        if len(find_six_element)==6:
            print("six product is present")
        else:
            print("six product is not present")
        while True:
            continue


        
Test = LoginTest()
# LoginTest.blank_field(Test)
# LoginTest.login_test(Test)
# LoginTest.locked_user(Test)       
# LoginTest.xbutton(Test)
# LoginTest.success_login(Test)
LoginTest.success_product(Test)

