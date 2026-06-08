import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


option = Options()
# option.add_argument("--headless")


driver = webdriver.Chrome(options=option)


driver.get("https://automationexercise.com/")
driver.maximize_window()

signinBtn= driver.find_element(By.XPATH , "//a[@href='/login']")
signinBtn.click()

wait= WebDriverWait(driver,10)
waitFD= WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])

loginEmail =wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@data-qa='login-email']")))
loginEmail.send_keys("john121@gmail.com")
loginPass = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[data-qa='login-password']")))
loginPass.send_keys("John123456")
loginBTN= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-qa='login-button']")))
loginBTN.click()

userName= driver.find_element(By.XPATH,"//b[text()='john']").text
print(userName)

assert userName == "john","Login is not success"
print("login succes with name John")

deletBtn= waitFD.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a[href='/delete_account']")))
deletBtn.click()

DeleMeg = driver.find_element(By.XPATH ,"//p[text()='Your account has been permanently deleted!']").text

assert "Your account has been permanently deleted!"==DeleMeg ,"Account is not deleted"
print(DeleMeg)