import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.mark.parametrize("search",[("pytest"),("hello"),("good")])
def test_search(search):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    search1 = driver.find_element(By.CSS_SELECTOR,"textarea[name='q']")
    search1.send_keys(search)
    time.sleep(5)
    driver.quit()