
from selenium.webdriver.common.by import By
from POM.Contactus_page import Contact




class Register_exist:
    def __init__(self,driver):
        self.driver=driver
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.login_click=(By.XPATH,"//a[@href='/login']")
        self.sign_up=(By.XPATH,"//h2[text()='New User Signup!']")
        self.signup_name=(By.XPATH,"//input[@data-qa='signup-name']")
        self.signup_email=(By.XPATH,"//input[@data-qa='signup-email']")
        self.signup_button=(By.XPATH,"//button[@data-qa='signup-button']")
        self.text_shown=(By.XPATH,"//p[text()='Email Address already exist!']")


    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_register_with_existing_email(self):
        self.driver.find_element(*self.home_page).is_displayed()
        self.driver.find_element(*self.login_click).click()
        self.driver.find_element(*self.sign_up).is_displayed()
        self.driver.find_element(*self.signup_name).send_keys("Lakshmigr")
        self.driver.find_element(*self.signup_email).send_keys("lakshmigr999@gmail.com")
        self.driver.find_element(*self.signup_button).click()
        self.driver.find_element(*self.text_shown).is_displayed()

        Contact_us=Contact(self.driver)
        return Contact_us