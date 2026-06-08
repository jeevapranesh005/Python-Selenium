import select
from sre_constants import BRANCH
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



driver = webdriver.Chrome()
driver.get("https://leafground.com/select.xhtml;jsessionid=node03f9nybsnp2bh13izxmj9ges6a17899653.node0")
driver.maximize_window
wait = WebDriverWait(driver,10)

# 1.method
driver.find_element(
    By.XPATH,
    "//label[@id='j_idt87:lang_label']"
).click()

dropdown= driver.find_elements(By.XPATH,"//ul[@id='j_idt87:lang_items']//li")

for drop in dropdown:
    if drop.text=="Tamil":
        drop.click()
        print(drop.text)
        break


# 2 method

driver.find_element(By.CSS_SELECTOR,"li[data-label='Tamil']").click()

# 3. Method - js


mal=driver.find_element(By.CSS_SELECTOR,"li[data-label='Malayalam']")
driver.execute_script("arguments[0].click();",mal)


time.sleep(10)