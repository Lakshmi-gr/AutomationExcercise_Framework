import time
from selenium.webdriver.common.by import By
from POM.add_to_cart import Addcart


class Subs_cart:
    def __init__(self,driver):
        self.driver=driver
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.cart=(By.XPATH,"//a[contains(text(),' Cart')]")
        self.cartsubs_email=(By.XPATH,"//input[@placeholder='Your email address']")
        self.arrowclick=(By.XPATH,"//i[@class='fa fa-arrow-circle-o-right']")
        self.subscription=(By.XPATH,"//h2[contains(text(),'Subscription')]")

    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_verify_subscription_cart(self):

        print(self.driver.find_element(*self.home_page).is_displayed())
        self.driver.find_element(*self.cart).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(10)
        self.driver.find_element(*self.cartsubs_email).send_keys("lakshmigr999@gmail.com")
        self.driver.find_element(*self.arrowclick).click()
        print(self.driver.find_element(*self.subscription).is_displayed())

        Add_to_Cart = Addcart(self.driver)
        return Add_to_Cart
