import pytest

from POM.Contactus_page import Contact

@pytest.mark.sanity
def test_contact_us(driver):
    contact = Contact(driver)
    contact.go_to_homepage()
    contact.test_contact_us_page()