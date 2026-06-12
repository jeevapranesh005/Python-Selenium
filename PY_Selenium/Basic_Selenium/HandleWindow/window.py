from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")

parent = driver.current_window_handle

driver.find_element(By.ID, "openWindow").click()

windows = driver.window_handles

for win in windows:
    if win != parent:
        driver.switch_to.window(win)
        break

print("Child Title:", driver.title)

driver.close()

driver.switch_to.window(parent)

print("Parent Title:", driver.title)