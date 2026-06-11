import pytest
from utilites import ExcelReader
from utilites import logCreator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin1:

    logger = logCreator.log_generator()

    @pytest.mark.parametrize(
        "username,password",
        ExcelReader.get_data(
            r"D:\python selenium-D\PY_pytest\TutuorialNinja_DataDriven\Excel\Book1.xlsx",
            "Sheet1"
        )
    )
    def test_login(self, username, password):

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']"))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
        ).click()

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='email']"))
        ).send_keys(username)

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        ).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']"))
        ).click()

        loginText = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'My Account')]"))
        ).text

        assert "My Account" in loginText


    @pytest.mark.search
    @pytest.mark.parametrize(
        "product",
        ExcelReader.get_data(
            r"D:\python selenium-D\PY_pytest\TutuorialNinja_DataDriven\Excel\Book1.xlsx",
            "search"
        )
    )
    def test_search(self, product):

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
        ).send_keys(product)

        self.driver.find_element(By.XPATH, "//span[@class='input-group-btn']").click()

        products = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//div[contains(@class,'product-layout')]")
            )
        )

        print(len(products))