import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.execute_cdp_cmd("Network.enable", {})

driver.execute_cdp_cmd(
    "Network.setBlockedURLs",
    {
        "urls": [
            "*googlesyndication.com*",
            "*adsbygoogle.js*",
            "*doubleclick.net*",
            "*googleads*"
        ]
    }
)

driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")


time.sleep(1000)