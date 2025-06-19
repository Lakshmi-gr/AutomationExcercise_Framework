import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from POM.check_out import CheckOut
#from selenium.webdriver.support import expected_conditions as EC



class ViewProduct:
    def __init__(self,driver):
        self.driver=driver
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.product_click=(By.XPATH,"//a[@href='/products']")
        self.product_details=(By.XPATH,"//a[@href='/product_details/1']")
        self.view_product=(By.XPATH,"//a[@href='/product_details/1' and contains(., 'View Product')]")
        self.quantity=(By.XPATH,"//input[@id='quantity']")
        self.add_to_cart=(By.XPATH,"//button[@class='btn btn-default cart' and contains(., 'Add to cart')]")


    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_view_product_check(self):

        print(self.driver.find_element(*self.home_page).is_displayed())
        self.driver.find_element(*self.product_click).click()
        wait=WebDriverWait(self.driver,10)
        element=self.driver.find_element(*self.product_details)
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
        print(element.is_displayed())
        main_window=self.driver.current_window_handle
        view_product=self.driver.find_element(*self.view_product)
        ActionChains(self.driver).key_down(Keys.CONTROL).click(view_product).key_up(Keys.CONTROL).perform()
        time.sleep(2)

        for handle in self.driver.window_handles:
            if handle!=main_window:
                self.driver.switch_to.window(handle)
                break

        time.sleep(5)
        qty_input=self.driver.find_element(*self.quantity)
        qty_input.click()
        qty_input.send_keys(Keys.ARROW_UP)
        time.sleep(2)
        qty_input.send_keys(Keys.ARROW_UP)
        print("Updated quantity:",qty_input.get_attribute("value"))

        time.sleep(5)
        self.driver.find_element(*self.add_to_cart).click()
        time.sleep(5)
        self.driver.back()

        Check_Out=CheckOut(self.driver)
        return Check_Out

