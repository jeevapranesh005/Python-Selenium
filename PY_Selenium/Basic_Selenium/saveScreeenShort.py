from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.save_screenshot("fillScreen.png")
logo = driver.find_element(By.CLASS_NAME, "lnXdpd")

logo.screenshot("google_logo.png")

print("Screenshot saved")