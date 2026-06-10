import time
import pytest
from Pages.Laptop_page import laptop
from Pages.Cart_page import cart
from utilites.conftest import setup_and_teardown
from utilites import logCreator

@pytest.mark.usefixtures("setup_and_teardown")
class TestCart:
    
    def test_laptop(self):
        
        lap = laptop(self.driver)

        lap.laptopCat()
        cartp=cart(self.driver)
        cartp.addToCart()
        time.sleep(5)

