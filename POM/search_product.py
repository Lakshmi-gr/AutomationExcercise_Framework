
from selenium.webdriver.common.by import By
from POM.verify_subscription import Subscription



class SearchProduct:
    def __init__(self,driver):
        self.driver=driver
        self.product_click=(By.XPATH,"//a[@href='/products']")
        self.all_products=(By.XPATH,"//h2[text()='All Products']")
        self.search_product=(By.XPATH,"//input[@placeholder='Search Product']")
        self.search=(By.XPATH,"//i[@class='fa fa-search']")
        self.title_visible=(By.XPATH,"//h2[@class='title text-center']")


    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_search_products(self):

        self.driver.find_element(*self.product_click).click()
        print(self.driver.find_element(*self.all_products).is_displayed())
        self.driver.find_element(*self.search_product).send_keys("stylish dress")
        self.driver.find_element(*self.search).click()
        print(self.driver.find_element(*self.title_visible).is_displayed())

        Verify_Subscription=Subscription(self.driver)
        return Verify_Subscription