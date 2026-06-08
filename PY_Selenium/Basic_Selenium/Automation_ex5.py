from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://automationexercise.com')
driver.maximize_window()

sigin = driver.find_element(by=By.XPATH , value="//a[@href='/login']")
sigin.click()

siginText = driver.find_element(by=By.XPATH ,value="//div[@class='signup-form']/child::h2").text

if(siginText=="New User Signup!"):
    print("New User Signup! is displayed")
else:
    print("not New User Signup! displayed")

name= driver.find_element(by=By.XPATH ,value="//input[@type='text']")
name.send_keys("ram")
username=driver.find_element(by=By.XPATH , value="//input[@data-qa='signup-email']")
username.send_keys("ram99f@gmail.com")

driver.find_element(by=By.XPATH ,value="//button[text()='Signup']").click()

text=driver.find_element(By.XPATH,"//p[text()='Email Address already exist!']").text
assert text =="Email Address already exist!","error not fount"
print("Program is fully correct")
