
from selenium.webdriver.common.by import By
from POM.loginwithwrong import loginWrong



class Loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.click_login=(By.XPATH,"//i[@class='fa fa-lock']")
        self.user_email=(By.NAME,"email")
        self.password=(By.NAME,"password")
        self.button=(By.XPATH,"//button[text()='Login']")
        self.home=(By.XPATH,"//i[@class='fa fa-home']")

    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")
        self.driver.save_screenshot("homepage_before_login.png")

    def test_loginwithcrct_credentials(self):
        self.driver.find_element(*self.click_login).click()
        self.driver.find_element(*self.user_email).send_keys("lakshmigr999@gmail.com")
        self.driver.find_element(*self.password).send_keys("jump2@pump")
        self.driver.find_element(*self.button).click()
        self.driver.find_element(*self.home).is_displayed()
        #driver.find_element(By.XPATH,"//a[@href='/delete_account']").click()
        #driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
        Login_wrong=loginWrong(self.driver)
        return Login_wrong