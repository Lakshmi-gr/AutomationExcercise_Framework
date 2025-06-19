import pytest

from POM.login_page import Loginpage
from POM.loginwithwrong import loginWrong
from POM.logout_page import LogOut

@pytest.mark.smoke
def test_login_with_valid_credentials(driver):
    login =Loginpage (driver)
    login.go_to_homepage()
    login.test_loginwithcrct_credentials()

@pytest.mark.regression
def test_login_with_wrong_credentials(driver):
    wrong =  loginWrong(driver)
    wrong.go_to_homepage()
    wrong.test_loginwithwrong_credentials()

@pytest.mark.sanity
def test_logout_user(driver):
    logout_user = LogOut(driver)
    logout_user.go_to_homepage()
    logout_user.test_logout_user()