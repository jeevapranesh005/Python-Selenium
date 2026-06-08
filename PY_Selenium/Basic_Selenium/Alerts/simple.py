from ast import arguments
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

simpleBTN= driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']")
driver.execute_script("arguments[0].click();",simpleBTN)
alert= driver.switch_to.alert
text= alert.text
alert.accept()
print(text)
time.sleep(3)