import select
from sre_constants import BRANCH
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
driver.get("https://leafground.com/select.xhtml;jsessionid=node03f9nybsnp2bh13izxmj9ges6a17899653.node0")
driver.maximize_window
wait = WebDriverWait(driver,10)

search =driver.find_element(By.CSS_SELECTOR,"input[id='j_idt87:auto-complete_input']")
search.send_keys("aws")
search.send_keys(Keys.ENTER)
time.sleep(10)
