import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CheckOut:
    def __init__(self,driver):
        self.driver=driver
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.add_to_cart1=(By.XPATH,"//a[@data-product-id='3' and contains(.,'Add to cart')]")
        self.continue_shopping=(By.XPATH,"//button[text()='Continue Shopping']")
        self.add_to_cart2=(By.XPATH,"//a[@data-product-id='19' and contains(.,'Add to cart')]")
        self.view_cart=(By.XPATH,"//u[text()='View Cart']")
        self.prcd_checkout=(By.XPATH,"//a[text()='Proceed To Checkout']")
        self.reg_login=(By.XPATH,"//u[text()='Register / Login']")
        self.email=(By.NAME,"email")
        self.password=(By.NAME,"password")
        self.login_button=(By.XPATH,"//button[text()='Login']")
        self.view_cart1=(By.XPATH,"//a[@href='/view_cart']")
        self.prcd_checkout1=(By.XPATH,"//a[text()='Proceed To Checkout']")
        self.place_order=(By.XPATH,"//a[text()='Place Order']")
        self.name_card=(By.XPATH,"//input[@data-qa='name-on-card']")
        self.card_number=(By.XPATH,"//input[@data-qa='card-number']")
        self.cvc_number=(By.XPATH,"//input[@data-qa='cvc']")
        self.expiry_month=(By.XPATH,"//input[@data-qa='expiry-month']")
        self.expiry_year=(By.XPATH,"//input[@data-qa='expiry-year']")
        self.submit=(By.XPATH,"//button[@id='submit']")
        self.order_placed=(By.XPATH,"//b[text()='Order Placed!']")
        self.continue_button=(By.XPATH,"//a[text()='Continue']")


    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_check_out_page(self):


        #self.driver.execute_script("window.scrollBy(0, 600);")
        wait=WebDriverWait(self.driver,10)
        try:
            add_to_cart = wait.until(EC.presence_of_element_located(self.add_to_cart1))
            self.driver.execute_script("arguments[0].scrollIntoView();", add_to_cart)
            time.sleep(1)
            add_to_cart.click()
        except Exception as e:
            self.driver.save_screenshot("add_to_cart_error.png")
            raise e

        self.driver.find_element(*self.continue_shopping).click()
        #self.driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)
        try:
            addtocart = wait.until(EC.presence_of_element_located(self.add_to_cart2))
            self.driver.execute_script("arguments[0].scrollIntoView();", addtocart)
            time.sleep(5)
            addtocart.click()
        except Exception as e:
            self.driver.save_screenshot("addtocart_error.png")
            raise e

        self.driver.find_element(*self.view_cart).click()
        self.driver.find_element(*self.prcd_checkout).click()
        self.driver.find_element(*self.reg_login).click()
        self.driver.find_element(*self.email).send_keys("lakshmigr999@gmail.com")
        self.driver.find_element(*self.password).send_keys("gudu@8296")
        self.driver.find_element(*self.login_button).click()

        self.driver.find_element(*self.view_cart1).click()
        self.driver.find_element(*self.prcd_checkout1).click()
        self.driver.find_element(*self.place_order).click()
        self.driver.find_element(*self.name_card).send_keys("LAKSHMI GR")
        self.driver.find_element(*self.card_number).send_keys("123456789012")
        self.driver.find_element(*self.cvc_number).send_keys("211")
        self.driver.find_element(*self.expiry_month).send_keys("Feb")
        self.driver.find_element(*self.expiry_year).send_keys("2027")
        self.driver.find_element(*self.submit).click()
        self.driver.find_element(*self.order_placed).is_displayed()
        self.driver.find_element(*self.continue_button).click()
        print(self.driver.find_element(*self.home_page).is_displayed())

