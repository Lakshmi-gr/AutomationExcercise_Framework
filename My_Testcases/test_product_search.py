import pytest

from POM.Testcase_page import Testcase
from POM.Product_page import Product_Page
from POM.search_product import SearchProduct

@pytest.mark.sanity
def test_test_case_page(driver):
    testpage = Testcase(driver)
    testpage.go_to_homepage()
    testpage.test_Test_case_page()

@pytest.mark.regression
def test_product_details(driver):
    pd = Product_Page(driver)
    pd.go_to_homepage()
    pd.test_Product_Details()

@pytest.mark.regression
def test_search_products(driver):
    search = SearchProduct(driver)
    search.go_to_homepage()
    search.test_search_products()