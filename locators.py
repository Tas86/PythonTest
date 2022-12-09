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

driver.get("https://rahulshettyacademy.com/angularpractice")
time.sleep(10)
print(driver.title)
print(driver.current_url)

#ID, Xpath, CSSSelectors, Classname, name, linkText --> locators
#.send_keys --> method
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234");
driver.find_element(By.ID, "exampleCheck1").click()
#No mattere the element on the page, you can create XPATH and CSS
#Example of syntax (usata da Vaskar)
#to create XPATH for any element: //tagname[@attribute='value']
#to create CSS is same as XPATH but you don t need // and @: tagname[attribute='value']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "input[type= 'text").send_keys("Fabio")
driver.find_element(By.XPATH, "//input[@value='option1']").click()
#create a variable to print the text to ensure it is coming as expected
message= driver.find_element(By.CLASS_NAME, "alert-success").text
time.sleep(10)
assert "blu" in message
print(message)
time.sleep(20)
