import pytest

from POM.View_product import ViewProduct
from POM.check_out import CheckOut

@pytest.mark.smoke
def test_view_product_before_checkout(driver):
    view = ViewProduct(driver)
    view.go_to_homepage()
    view.test_view_product_check()

@pytest.mark.regression
def test_checkout_page(driver):
    checkout = CheckOut(driver)
    checkout.go_to_homepage()
    checkout.test_check_out_page()