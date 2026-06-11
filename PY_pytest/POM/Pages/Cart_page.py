
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class cart:

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver,10)

    addTocat = (By.XPATH,"//a[text()='Add to cart']")
    cart=(By.XPATH,"//a[text()='Cart']")
    placeOrder=(By.XPATH,"//button[@data-toggle='modal']")
    def addToCart(self):
        self.wait.until(EC.element_to_be_clickable((self.addTocat))).click()
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        self.wait.until(EC.element_to_be_clickable((self.cart))).click()
        self.wait.until(EC.element_to_be_clickable((self.placeOrder)))

    
