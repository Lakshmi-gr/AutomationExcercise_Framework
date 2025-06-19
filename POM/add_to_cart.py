import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.View_product import ViewProduct



class Addcart:
    def __init__(self,driver):
        self.driver=driver
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.product_click=(By.XPATH,"//a[@href='/products']")
        self.addto_cart=(By.XPATH,"//a[@data-product-id='3' and contains(.,'Add to cart')]")
        self.continue_shopping=(By.XPATH,"//button[text()='Continue Shopping']")
        self.addto_cart1=(By.XPATH,"//a[@data-product-id='19' and contains(.,'Add to cart')]")
        self.view_cart=(By.XPATH,"//u[text()='View Cart']")

    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_add_to_cart_products(self):

        print(self.driver.find_element(*self.home_page).is_displayed())
        self.driver.find_element(*self.product_click).click()
        wait=WebDriverWait(self.driver,10)
        add_to_cart=wait.until(EC.visibility_of_element_located(self.addto_cart))
        self.driver.execute_script("arguments[0].scrollIntoView();",add_to_cart)
        add_to_cart.click()
        time.sleep(15)
        self.driver.find_element(*self.continue_shopping).click()
        wait=WebDriverWait(self.driver,10)
        add_to_cart1=wait.until(EC.visibility_of_element_located(self.addto_cart1))
        self.driver.execute_script("arguments[0].scrollIntoView();",add_to_cart1)
        add_to_cart1.click()
        time.sleep(15)
        self.driver.find_element(*self.view_cart).click()

        View_Product=ViewProduct(self.driver)
        return View_Product
