import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_function():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.hyrtutorials.com/")

def teardown_function():
    driver.quit()

def test_valid():
    arr= driver.find_element(By.XPATH,"(//a[text()='Arrays in Java'])[1]")
    driver.execute_script("arguments[0].scrollIntoView();",arr)
    print("scrolled")

