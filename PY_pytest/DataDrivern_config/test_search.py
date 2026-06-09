from selenium.webdriver.common.by import By
import pytest
import pytest_check as check
from read_config import get_config


@pytest.mark.usefixtures("setup_and_teardown")
class Testsearch:

    search1 = get_config("search term","valid")
    search_invalid = get_config("search term","invalid")

    @pytest.mark.order(3)
    @pytest.mark.valid
    def test_validproduct(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(self.search1)

        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()

        check.is_true(self.driver.find_element(By.XPATH,"//img[@title='Canon EOS 5D']").is_displayed(),"Canon product is not displayed")
    @pytest.mark.order(2)
    def test_invalidproduct(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(self.search_invalid)

        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()

        actual_text = self.driver.find_element(By.XPATH,"//p[contains(text(),'There is no product that matches the search criter')]").text

        check.equal(actual_text,"There is no product that matches the search criteria.","Invalid product message mismatch")
    @pytest.mark.order(1)
    @pytest.mark.valid
    def test_noproduct(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("")

        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()

        actual_text = self.driver.find_element( By.XPATH,"//p[contains(text(),'There is no product that matches the search criter')]").text

        check.equal(actual_text, "There is no product that matches the search criteria.","No product search message mismatch")