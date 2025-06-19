import time
from selenium.webdriver.common.by import By
from POM.verify_subs_cart import Subs_cart



class Subscription:
    def __init__(self,driver):
        self.driver=driver
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.verify_email=(By.XPATH,"//input[@placeholder='Your email address']")
        self.arrow_click=(By.XPATH,"//i[@class='fa fa-arrow-circle-o-right']")
        self.subscription=(By.XPATH,"//h2[contains(text(),'Subscription')]")

    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_verify_subscription(self):
        print(self.driver.find_element(*self.home_page).is_displayed())
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(10)
        self.driver.find_element(*self.verify_email).send_keys("lakshmigr999@gmail.com")
        self.driver.find_element(*self.arrow_click).click()
        print(self.driver.find_element(*self.subscription).is_displayed())

        cart_subscription=Subs_cart(self.driver)
        return cart_subscription



