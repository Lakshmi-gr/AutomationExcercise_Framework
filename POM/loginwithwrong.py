
from selenium.webdriver.common.by import By
from POM.logout_page import LogOut




class loginWrong:
    def __init__(self,driver):
        self.driver=driver
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.login_click=(By.XPATH,"//i[@class='fa fa-lock']")
        self.email=(By.NAME,"email")
        self.passwod=(By.NAME,"password")
        self.login_button=(By.XPATH,"//button[text()='Login']")
        self.text_visible=(By.XPATH,"//p[text()='Your email or password is incorrect!']")

    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")


    def test_loginwithwrong_credentials(self):
        self.driver.find_element(*self.home_page).is_displayed()
        self.driver.find_element(*self.login_click).click()
        self.driver.find_element(*self.email).send_keys("lakshm74@gmail.com")
        self.driver.find_element(*self.passwod).send_keys("jfds#78")
        self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.text_visible).is_displayed()

        Log_out=LogOut(self.driver)
        return Log_out