import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from POM.login_page import Loginpage




class Register:
    def __init__(self,driver):
        self.driver=driver
        self.login_click=(By.XPATH,"//a[@href='/login']")
        self.signup_name=(By.XPATH,"//input[@data-qa='signup-name']")
        self.signup_email=(By.XPATH,"//input[@data-qa='signup-email']")
        self.signup_button=(By.XPATH,"//button[@data-qa='signup-button']")
        self.title=(By.XPATH,"//input[@value='Mrs']")
        self.signup_password=(By.XPATH,"//input[@type='password']")
        self.day=(By.XPATH,"//select[@data-qa='days']")
        self.month=(By.XPATH,"//select[@data-qa='months']")
        self.year=(By.XPATH,"//select[@data-qa='years']")
        self.signup_checkbox=(By.XPATH,"//label[text()='Sign up for our newsletter!']")
        self.offer_checkbox=(By.XPATH,"//label[text()='Receive special offers from our partners!']")
        self.first_name=(By.ID,"first_name")
        self.last_name=(By.ID,"last_name")
        self.address=(By.ID,"address1")
        self.country=(By.ID,"country")
        self.state=(By.ID,"state")
        self.country_name=(By.XPATH,"//option[text()='India']")
        self.city=(By.ID,"city")
        self.zipcode=(By.ID,"zipcode")
        self.mobile_number=(By.ID,"mobile_number")
        self.create_button=(By.XPATH,"//button[text()='Create Account']")
        self.continue_button=(By.XPATH,"//a[@data-qa='continue-button']")
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.delete_account=(By.XPATH,"//a[@href='/delete_account']")
        self.continuebutton=(By.XPATH,"//a[@data-qa='continue-button']")


    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")



    def test_Register_user(self):

        self.driver.find_element(*self.login_click).click()
        self.driver.find_element(*self.signup_name).send_keys("kavyaby")
        self.driver.find_element(*self.signup_email).send_keys("kavya456@gmail.com")
        self.driver.find_element(*self.signup_button).click()
        self.driver.find_element(*self.title).click()
        self.driver.find_element(*self.signup_password).send_keys("pymur@78")
        #dropdowns
        Select(self.driver.find_element(*self.day)).select_by_value("1")
        Select(self.driver.find_element(*self.month)).select_by_visible_text("February")
        Select(self.driver.find_element(*self.year)).select_by_value("2000")
        self.driver.find_element(*self.signup_checkbox).click()
        self.driver.find_element(*self.offer_checkbox).click()
        self.driver.find_element(*self.first_name).send_keys("Lakshmi")
        self.driver.find_element(*self.last_name).send_keys("GR")
        self.driver.find_element(*self.address).send_keys("111# 3rd cross banglore Karnataka")
        self.driver.find_element(*self.country).click()
        self.driver.find_element(*self.country_name)
        self.driver.find_element(*self.state).send_keys("Karnataka")
        self.driver.find_element(*self.city).send_keys("banglore")
        self.driver.find_element(*self.zipcode).send_keys("560059")
        self.driver.find_element(*self.mobile_number).send_keys("9451205376")
        self.driver.find_element(*self.create_button).click()

        self.driver.find_element(*self.continue_button).click()
        self.driver.find_element(*self.home_page).is_displayed()
        self.driver.find_element(*self.delete_account).click()
        self.driver.find_element(*self.continuebutton).click()

        Login_page=Loginpage(self.driver)
        return Login_page
















