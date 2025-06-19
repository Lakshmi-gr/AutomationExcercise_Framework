import time



from selenium import webdriver
from POM.Home_page import Register



def test_automation(driver):

    driver.get("http://automationexercise.com")
    driver.implicitly_wait(15)

    Home=Register(driver)
    Login=Home.test_Register_user()
    LoginWrong=Login.test_loginwithcrct_credentials()
    LogOut=LoginWrong.test_loginwithwrong_credentials()
    ExistingEmail=LogOut.test_logout_user()
    Contact=ExistingEmail.test_register_with_existing_email()
    Testcase=Contact.test_contact_us_page()
    Product=Testcase.test_Test_case_page()
    Search=Product.test_Product_Details()
    Subscription=Search.test_search_products()
    cart_Subscription=Subscription.test_verify_subscription()
    AddToCart=cart_Subscription.test_verify_subscription_cart()
    ViewProduct=AddToCart.test_add_to_cart_products()
    Check_Out=ViewProduct.test_view_product_check()
    Check_Out.test_check_out_page()






