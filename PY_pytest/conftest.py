# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# @pytest.fixture()
# def setup(request):
#     driver = webdriver.Chrome()
#     action = ActionChains(driver)
#     driver.execute_cdp_cmd("Network.enable", {})

#     driver.execute_cdp_cmd(
#         "Network.setBlockedURLs",
#         {
#             "urls": [
#                 "*adsbygoogle*",
#                 "*show_ads_impl*",
#                 "*googlesyndication.com*",
#                 "*doubleclick.net*",
#                 "*zrt_lookup*",
#                 "*pagead2.googlesyndication.com*",
#                 "*googleads.g.doubleclick.net*",
#                 "*ads?client=*"
#             ]
#         }
#     )
#     driver.maximize_window()
#     driver.implicitly_wait(10)

#     driver.get("https://www.hyrtutorials.com/")
#     request.cls.driver=driver
#     yield driver

#     driver.quit()

import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome","edge"])
def setup_and_teardown(request):
    if request.param=="chrome":
        driver = webdriver.Chrome()
    elif request.param=="edge":
        driver=webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.hyrtutorials.com/")
    request.cls.driver=driver
    yield
    driver.quit()