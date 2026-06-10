import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites import logCreator

class laptop:
    logger=logCreator.log_generator()
    laptop=(By.XPATH,"//a[text()='Laptops']")
    sonyLap=(By.XPATH,"//a[text()='Sony vaio i5']")


    def __init__(self,driver):
        self.driver=driver
        self.wait= WebDriverWait(self.driver,10)

    def laptopCat(self):
        self.wait.until(EC.visibility_of_element_located((self.laptop))).click()
        self.logger.info("the laptop category is opened")
        self.wait.until(EC.visibility_of_element_located((self.sonyLap))).click()
        self.logger.info("the SonyLap is clicked")
        

    


        