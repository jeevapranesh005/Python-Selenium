import select
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")
driver.maximize_window()
wait = WebDriverWait(driver,10)


dropdown= driver.find_element(By.XPATH,"//select[@id='ide']")
select = Select(dropdown)
select.select_by_index(2)
select.select_by_value("ec")

curtSele= select.all_selected_options
for i in curtSele:
    print(i.text)


select.deselect_by_index(0)
select.deselect_all()


mul=select.is_multiple
print(mul)



time.sleep(10)