#Task to display cookies before login and after login in https://www.saucedemo.com/
# Using Exceptional handling to write Python Selenium codes

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class Followers_Following:
  
   #constructor
   def __init__(self):
       self.url = "https://www.saucedemo.com/"
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))  

    #To extract the data and print the values
   def login(self):
       
       try:        
            self.driver.get(self.url)
            sleep(2)

            # To cookie before login
            before_login_cookie= self.driver.get_cookies()
            sleep(2)

            # login
            self.driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")
            self.driver.find_element(by=By.ID, value="password").send_keys("secret_sauce")
            self.driver.find_element(by=By.XPATH, value='//*[@id="login-button"]').click()
            sleep(2)
            
            after_login_cookie= self.driver.get_cookies()
            sleep(2)
       except NoSuchElementException as selenium_error:
           print("Element not found", selenium_error)
       finally:
            #To print the values
            print("Before Login Cookie ", before_login_cookie)
            print("After Login Cookie ", after_login_cookie)
            self.driver.quit()


   

FF = Followers_Following()
FF.login()

