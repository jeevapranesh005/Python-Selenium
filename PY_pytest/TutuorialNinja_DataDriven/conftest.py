import pytest
from selenium import webdriver
from read_config import get_config
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def setup_and_teardown(request):

    browser = get_config("basic info", "browser")
    url = get_config("basic info", "url")

    driver = None

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    else:
        raise Exception(f"Browser not supported: {browser}")

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)

    yield

    driver.quit()