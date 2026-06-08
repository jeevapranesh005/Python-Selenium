import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.hyrtutorials.com/")

    yield driver

    driver.quit()


def test_home_page(setup):

    print("Current URL :", setup.current_url)
    print("Page Title  :", setup.title)

    assert "hyrtutorials" in setup.current_url.lower(), "URL is incorrect"
    assert setup.title != "", "Page title should not be empty"

    print("Home page test passed!")


def test_scroll_element(setup):

    ele = setup.find_element(
        By.XPATH,
        "(//a[text()='Write a java program to print the factors of a given number'])[1]"
    )

    setup.execute_script(
        "arguments[0].scrollIntoView();",
        ele
    )

    print("Scrolled to element successfully")