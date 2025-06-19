import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.Testcase_page import Testcase



class Contact:
    def __init__(self,driver):
        self.driver=driver
        self.home_page=(By.XPATH,"//i[@class='fa fa-home']")
        self.contactus_click=(By.XPATH,"//a[@href='/contact_us']")
        self.getin_touch=(By.XPATH,"//h2[text()='Get In Touch']")
        self.name=(By.XPATH,"//input[@data-qa='name']")
        self.email=(By.XPATH,"//input[@data-qa='email']")
        self.subject=(By.XPATH,"//input[@data-qa='subject']")
        self.message=(By.XPATH,"//textarea[@data-qa='message']")
        self.input_file=(By.XPATH,"//input[@type='file']")
        self.submit=(By.XPATH,"//input[@type='submit']")
        self.success_message=(By.XPATH,"//div[@class='status alert alert-success']")
        self.arrow_click=(By.XPATH,"//i[@class='fa fa-angle-double-left']")



    def go_to_homepage(self):
        self.driver.get("https://automationexercise.com")

    def test_contact_us_page(self):
        print(self.driver.find_element(*self.home_page).is_displayed())
        self.driver.find_element(*self.contactus_click).click()
        self.driver.find_element(*self.getin_touch).is_displayed()
        self.driver.find_element(*self.name).send_keys("Lakshmigr")
        self.driver.find_element(*self.email).send_keys("lakshmigr999@gmail.com")
        self.driver.find_element(*self.subject).send_keys("product")
        self.driver.find_element(*self.message).send_keys("im facing issue with ordering a product")


        wait=WebDriverWait(self.driver,10)
        upload_element=wait.until(EC.presence_of_element_located(self.input_file))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_element)

        upload_element.send_keys("C:/Users/ravit/OneDrive/Pictures/133858036258877848.jpg")
        time.sleep(10)
        self.driver.find_element(*self.submit).click()
        time.sleep(10)
        alert=self.driver.switch_to.alert
        alert.accept()
        time.sleep(10)
        print(self.driver.find_element(*self.success_message).is_displayed())
        self.driver.find_element(*self.arrow_click).click()

        Test_Case=Testcase(self.driver)
        return Test_Case

