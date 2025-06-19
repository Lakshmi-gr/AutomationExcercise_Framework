from POM.registerwithexistingmail import Register_exist


def test_register_with_existing_email(driver):
    reg = Register_exist(driver)
    reg.go_to_homepage()
    reg.test_register_with_existing_email()