from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()

wait = WebDriverWait(driver,10,poll_frequency=2)

driver.get("http://automationexercise.com")
driver.maximize_window()

wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/login']"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@data-qa='login-email']"))).send_keys("ram99f@gmail.com")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[data-qa='login-password']"))).send_keys("ram123456")
driver.find_element(By.CSS_SELECTOR,"button[data-qa='login-button']").click()


userName= driver.find_element(By.XPATH,"//b[text()='ram']").text
print(userName)

assert userName == "ram","Login is not success"
print("login succes with name John")
logout=driver.find_element(By.CSS_SELECTOR,"a[href='/logout']")
logout.click()

loginText=wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[text()='Login to your account']"))).text

assert "Login to your account"==loginText,"Login is not open"
print(loginText)