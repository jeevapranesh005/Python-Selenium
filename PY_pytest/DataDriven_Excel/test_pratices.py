import pytest
import time
from selenium import webdriver
from utilites import ExcelReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites import logCreator

from selenium.webdriver.common.by import By

class TestLogin1:
    logger=logCreator.log_generator()
    @pytest.mark.parametrize("username,password", ExcelReader.get_data(r"D:\python selenium-D\PY_pytest\DataDriven_Excel\Excel\Book1.xlsx","Sheet1")
    )
    def test_login(self, username, password):

        self.driver = webdriver.Chrome()

        self.driver.get("https://demoblaze.com/#")
        self.driver.maximize_window()
        self.logger.info("website is lanuched")

        wait = WebDriverWait(self.driver, 10)

        
        wait.until(EC.visibility_of_element_located((By.ID,"login2"))).click()
        self.logger.info("login page is opened")

        username_txt = wait.until(
            EC.visibility_of_element_located((By.ID, "loginusername"))
        )
        username_txt.send_keys(username)

        password_txt = wait.until(
            EC.visibility_of_element_located((By.ID, "loginpassword"))
        )
        password_txt.send_keys(password)
        self.logger.info("username and password is entered")
        
        LoginBTN=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@onclick='logIn()']")))
        LoginBTN.click()

        wel = wait.until(EC.visibility_of_element_located((By.ID,"nameofuser")))
        assert wel.text=="Welcome jeevs"
        print("login is succesfull")
        self.logger.error("login is succesfull")

        logoutBTN = wait.until(EC.visibility_of_element_located((By.ID,"logout2")))
        logoutBTN.click()
    
        self.driver.quit()