import time
import pytest
from Pages.Login_page import Login
from selenium import webdriver
from utilites.conftest import setup_and_teardown
from utilites import logCreator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from configration.read_config import get_config



@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    logger=logCreator.log_generator()
    def test_login(self):

        Username=get_config("valid","username")
        password=get_config("valid","password")
        login = Login(self.driver)  

        login.click_login()
        self.logger.info("login page is open")
        login.enter_username(Username)
        login.enter_password(password)
        self.logger.info("valid login details is Entered")
        login.click_button()
        act=self.wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@id='nameofuser']"))).text
        assert act=="Welcome jeevs"
        self.logger.info("Login is succesfull")
        time.sleep(10)