import pytest

from POM.verify_subs_cart import Subs_cart
from POM.add_to_cart import Addcart

@pytest.mark.regression
def test_subscription_on_cart_page(driver):
    subs = Subs_cart(driver)
    subs.go_to_homepage()
    subs.test_verify_subscription_cart()

@pytest.mark.smoke
def test_add_to_cart_products(driver):
    cart = Addcart(driver)
    cart.go_to_homepage()
    cart.test_add_to_cart_products()