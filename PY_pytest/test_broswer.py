import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options



@pytest.mark.parametrize("browser",["chrome","edge"])
@pytest.mark.parametrize("Website",['https://www.flipkart.com/','https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=808942225170&hvpos=&hvnetw=g&hvrand=8016480244331698961&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9299467&hvtargid=kwd-10573980&hydadcr=14453_2459472&gad_source=1'])
def test_browse(browser,Website):

    driver=None
    option= Options()

    if browser=="chrome":
        #option.add_argument("--headless")
        driver = webdriver.Chrome(option)
        print("chrome")
    if browser=="edge":
        #option.add_argument("--headless")
        driver = webdriver.Edge(option)
        print("edge")
    
    driver.maximize_window()
    driver.get(Website)
    print(driver.title)
    driver.quit()
