import pytest
import time
from selenium import webdriver
from utilites import ExcelReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites import logCreator
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin1:
    
    logger=logCreator.log_generator()
    @pytest.mark.parametrize("username,password", ExcelReader.get_data(r"D:\python selenium-D\PY_pytest\TutuorialNinja_DataDriven\Excel\Book1.xlsx","Sheet1")
    )
    def test_login(self, username, password):
       
        self.wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='My Account']"))).click()
        self.logger.info("Clicking the My account")
        self.wait.until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Login']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='email']"))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='password']"))).send_keys(password)
        self.logger.info("Enter the email and password")
        self.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@value='Login']"))).click()
        loginText = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[text()='My Account']"))).text
        assert loginText =="My Account"
        self.logger.info("login the user is successfull")
    @pytest.mark.search
    @pytest.mark.parametrize("product",ExcelReader.get_data(r"D:\python selenium-D\PY_pytest\TutuorialNinja_DataDriven\Excel\Book1.xlsx","search"))
    def test_search(self,product):
        self.logger.info("user search the product")
        self.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Search']"))).send_keys(product)
        self.driver.find_element(By.XPATH,"//span[@class='input-group-btn']").click()
        self.logger.info("the user seen the product")
     

        count=self.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12']")))
        print(len(count))
        
        

