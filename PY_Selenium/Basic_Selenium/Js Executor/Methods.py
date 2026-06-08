
import time

from outcome import Value
from pygments import highlight
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/?utm_source=chatgpt.com")
driver.maximize_window()


#1. click
# clickEle = driver.find_element(By.XPATH,"//a[text()='Udemy Courses']")
# driver.execute_script("arguments[0].click();",clickEle)
# driver.back()

#2. scrollto element
# scrollEle = driver.find_element(By.XPATH,"//h2[text()='Dynamic Web Table']")
# driver.execute_script("arguments[0].scrollIntoView();",scrollEle)

#3. enter Value
enterText = driver.find_element(By.ID,"name")
driver.execute_script("arguments[0].value='Jeeva';",enterText)

#4.getText
getText = driver.find_element(By.CSS_SELECTOR,"label[for='colors']")
text =driver.execute_script(" return arguments[0].innerText;",getText)
print(text)


#5. highlight element

ele = driver.find_element(By.XPATH,"//a[text()='GUI Elements']")
driver.execute_script("arguments[0].style.border='3px solid red';",ele)


