import select
from sre_constants import BRANCH
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.execute_cdp_cmd("Network.enable", {})

driver.execute_cdp_cmd(
    "Network.setBlockedURLs",
    {
        "urls": [
            "*adsbygoogle*",
            "*show_ads_impl*",
            "*googlesyndication.com*",
            "*doubleclick.net*",
            "*zrt_lookup*",
            "*pagead2.googlesyndication.com*",
            "*googleads.g.doubleclick.net*",
            "*ads?client=*"
        ]
    }
)



driver.get("https://www.hyrtutorials.com/")
driver.maximize_window()
action = ActionChains(driver)

sel = driver.find_element(By.XPATH,"//a[text()='Selenium Practice']")
action.move_to_element(sel).perform()
ele = driver.find_element(By.XPATH,"//a[text()='Window Handles']")
action.click(ele).perform()
time.sleep(10)