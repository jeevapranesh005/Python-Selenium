from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.execute_cdp_cmd("Network.enable", {})

driver.execute_cdp_cmd(
    "Network.setBlockedURLs",
    {
        "urls": [
            "*adsbygoogle*",
            "*googlesyndication.com*",
            "*show_ads*",
            "*adslots*",
            "*doubleclick.net*"
        ]
    }
)

driver.get("https://automationexercise.com/")

time.sleep(1000)