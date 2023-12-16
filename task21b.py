#Task to display cookies before login and after login Zenportal
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
       self.url = "https://www.zenclass.in/login"
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
            self.driver.find_element(by=By.NAME, value="email").send_keys("sadiqua.avril17@gmail.com")
            self.driver.find_element(by=By.NAME, value="password").send_keys("K@leem5800")
            self.driver.find_element(by=By.XPATH, value='//button[@class="col-md-12 btn btn-lg btn-block login-btn mt-4 mb-4"]').click()
            sleep(2)
            
            # To cookie after login
            after_login_cookie= self.driver.get_cookies()
            sleep(2)
       except NoSuchElementException as selenium_error:
           print("Element not found", selenium_error)
       finally:
            #To print the values
            print("Before Login Cookie ", before_login_cookie)
            print("After Login Cookie ", after_login_cookie)
            self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/nav/div/div/div/div/button[2]').click()
            sleep(2)
            self.driver.quit()
    

FF = Followers_Following()
FF.login()

