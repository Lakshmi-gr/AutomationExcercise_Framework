
from selenium.webdriver.common.by import By
from POM.Product_page import Product_Page


class Testcase:
    def __init__(self,driver):
        self.driver=driver
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.testcase_click=(By.XPATH,"//a[@href='/test_cases']")
        self.test_cases=(By.XPATH,"//b[text()='Test Cases']")



    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_Test_case_page(self):
        print(self.driver.find_element(*self.home_page).is_displayed())
        self.driver.find_element(*self.testcase_click).click()
        self.driver.find_element(*self.test_cases).is_displayed()

        Products=Product_Page(self.driver)
        return Products
