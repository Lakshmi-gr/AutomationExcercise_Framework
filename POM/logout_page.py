
from selenium.webdriver.common.by import By
from POM.registerwithexistingmail import Register_exist





class LogOut:
    def __init__(self,driver):
        self.driver=driver
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.login_click=(By.XPATH,"//i[@class='fa fa-lock']")
        self.logon_to_account=(By.XPATH,"//h2[text()='Login to your account']")
        self.email=(By.NAME,"email")
        self.password=(By.NAME,"password")
        self.login_button=(By.XPATH,"//button[text()='Login']")
        self.visible_text=(By.XPATH,"//a[text()=' Logged in as ']")
        self.logout_button=(By.XPATH,"//a[@href='/logout']")
        self.loginto_account=(By.XPATH,"//h2[text()='Login to your account']")


    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_logout_user(self):
        self.driver.find_element(*self.home_page).is_displayed()
        self.driver.find_element(*self.login_click).click()
        self.driver.find_element(*self.logon_to_account).is_displayed()
        self. driver.find_element(*self.email).send_keys("lakshmigr999@gmail.com")
        self.driver.find_element(*self.password).send_keys("gudu@8296")
        self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.visible_text).is_displayed()
        self.driver.find_element(*self.logout_button).click()
        self.driver.find_element(*self.loginto_account).is_displayed()

        Existing_email=Register_exist(self.driver)
        return Existing_email