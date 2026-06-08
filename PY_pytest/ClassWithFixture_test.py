import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures("setup")
class TestSearch:
    def test_valid(self):
        action = ActionChains(self.driver)

        menu = self.driver.find_element(
            By.XPATH,
            "//a[text()='Selenium Practice']"
        )

        action.move_to_element(menu).perform()

        window_handle = self.driver.find_element( By.XPATH, "//a[text()='Window Handles']")

        window_handle.click()

