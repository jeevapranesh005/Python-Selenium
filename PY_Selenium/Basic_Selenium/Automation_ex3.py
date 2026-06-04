
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

from soft_assert import SoftAssert

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10,poll_frequency=2)


driver.get("https://automationexercise.com/")
driver.maximize_window()

signinBtn= driver.find_element(By.XPATH , "//a[@href='/login']")
signinBtn.click()


loginEmail =wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@data-qa='login-email']")))
loginEmail.send_keys("john121@gmail.com")
loginPass = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[data-qa='login-password']")))
loginPass.send_keys("John123456")
loginBTN= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-qa='login-button']")))
loginBTN.click()
print("clicked")

Error= wait.until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Your email or password is incorrect!']"))).text

sa = SoftAssert()

