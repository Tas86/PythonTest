from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import StaleElementReferenceExeption
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

#service_obj = Service
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])
#driver = webdriver

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                          options=chromeOptions,
                          desired_capabilities=chromeOptions.to_capabilities())

#driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.set_script_timeout(5)
driver.maximize_window()
wait = WebDriverWait(driver, 10, 1)

driver.get("https://rahulshettyacademy.com")
time.sleep(10)
print(driver.title)
print(driver.current_url)

#find search box
Find_searchbox =

