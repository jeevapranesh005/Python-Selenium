import select
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")
driver.maximize_window
wait = WebDriverWait(driver,10)


dropdown= driver.find_element(By.XPATH,"//select[@id='course']")
select = Select(dropdown)
select.select_by_index(2)
select.select_by_value("python")
select.select_by_visible_text("Dot Net")

first =select.first_selected_option
print(first.text)
select.deselect_all
opt= select.options

for i in opt:
    print(i.text)


time.sleep(10)
