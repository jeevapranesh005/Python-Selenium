import pytest
from selenium import webdriver
from read_config import get_config

@pytest.fixture
def setup_and_teardown(request):

    browser = get_config("basic info", "browser")
    url = get_config("basic info", "url")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()

    elif browser.lower() == "edge":
        driver = webdriver.Edge()

    else:
        raise Exception(f"Unsupported browser: {browser}")

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver

    yield

    driver.quit()