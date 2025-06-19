import time
from selenium.webdriver.common.by import By
from POM.search_product import SearchProduct




class Product_Page:
    def __init__(self,driver):
        self.driver=driver
        self.product_click=(By.XPATH,"//a[@href='/products']")
        self.products_display=(By.XPATH,"//h2[text()='All Products']")
        self.product_details=(By.XPATH,"//a[@href='/product_details/1']")
        self.view_product=(By.XPATH,"//a[.//i[@class='fa fa-plus-square'] and contains(text(),'View Product')]")
        self.brands_displayed=(By.XPATH,"//h2[text()='Brands']")

    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_Product_Details(self):
        self.driver.find_element(*self.product_click).click()
        print(self.driver.find_element(*self.products_display).is_displayed())
        element=self.driver.find_element(*self.product_details)
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
        print(element.is_displayed())
        self.driver.find_element(*self.view_product).click()
        time.sleep(10)
        print(self.driver.find_element(*self.brands_displayed).is_displayed())
        time.sleep(10)

        Search_Product=SearchProduct(self.driver)
        return Search_Product