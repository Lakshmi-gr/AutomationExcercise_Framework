import pytest
from POM.verify_subscription import Subscription

@pytest.mark.sanity
def test_subscription_footer(driver):
    sub = Subscription(driver)
    sub.go_to_homepage()
    sub.test_verify_subscription()