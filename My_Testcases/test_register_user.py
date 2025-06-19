import pytest
from POM.Home_page import Register

@pytest.mark.smoke
@pytest.mark.regression
def test_register_user(driver):
    driver.get("https://automationexercise.com")
    register_page = Register(driver)
    register_page.go_to_homepage()
    register_page.test_Register_user()

