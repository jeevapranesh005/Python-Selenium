import time
import pytest
from Pages.Laptop_page import laptop
from utilites.conftest import setup_and_teardown
from utilites import logCreator

@pytest.mark.dependency(depends=["test_login"])
@pytest.mark.usefixtures("setup_and_teardown")
class TestLaptopSearch:
    logger=logCreator.log_generator()
    def test_laptop(self):

        lap = laptop(self.driver)
        lap.laptopCat()
        self.logger.info("Laptop page is oped..")
        