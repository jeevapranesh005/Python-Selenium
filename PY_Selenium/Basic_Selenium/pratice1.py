import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()

print(driver.title)
search = driver.find_element(By.NAME, value="q")


# if(search.is_enabled):
#     print("enable")
# else:
#     print("not enable")


var =search.send_keys("Selenium Python")
time

driver.quit()