from re import X
import time
from xml.etree.ElementPath import xpath_tokenizer

from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_config import get_config




@pytest.mark.usefixtures("setup_and_teardown")
class Testsearch:

    

    def test_login(self):
        name = get_config("login","username")
        password = get_config("login","password")
        wait=WebDriverWait(self.driver,10)
        self.driver.find_element(By.ID,"login2").click()
        username=wait.until(EC.visibility_of_element_located((By.ID,"loginusername")))
        username.send_keys(self.name)
        
        Pass=wait.until(EC.visibility_of_element_located((By.ID,"loginpassword")))
        Pass.send_keys(self.password)
        
        LoginBTN=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@onclick='logIn()']")))
        LoginBTN.click()

        wel = wait.until(EC.visibility_of_element_located((By.ID,"nameofuser")))
        assert wel.text=="Welcome jeevs"
        print("login is succesfull")
        time.sleep(5)