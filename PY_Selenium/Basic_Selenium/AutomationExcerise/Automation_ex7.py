import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Chrome()

driver.get('http://automationexercise.com')
driver.maximize_window()

action = ActionChains(driver)
testCase = driver.find_element(By.XPATH,"//a[@href='/test_cases']")

action.click(testCase).perform()

testCaseText = driver.find_element(By.XPATH,"//b[text()='Test Cases']").text
print(testCaseText)