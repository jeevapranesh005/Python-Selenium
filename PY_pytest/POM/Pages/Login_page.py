from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    login_link = (By.ID, "login2")
    username_txt = (By.ID, "loginusername")
    user_password=(By.ID,"loginpassword")
    button=(By.XPATH,"//button[@onclick='logIn()']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_login(self):
        self.driver.find_element(*self.login_link).click()

    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located(self.username_txt)
        ).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.user_password).send_keys(password)
    
    def click_button(self):
        self.wait.until(EC.visibility_of_element_located((self.button))).click()
        