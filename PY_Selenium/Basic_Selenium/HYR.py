import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/")
action = ActionChains(driver)

SelPratice =driver.find_element(By.XPATH,"//a[text()='Selenium Practice']")
action.move_to_element(SelPratice)
windowPratice = driver.find_element(By.XPATH,"//a[text()='Window Handles']")
action.click(windowPratice) 
windowText= driver.find_element(By.XPATH,"h1[itemprop='name']").text
print(windowText)

time.sleep(4)
