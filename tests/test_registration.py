import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con
from helpers.randomizer import generate_name, generate_email, generate_password
from helpers.locators import Locators


@pytest.mark.usefixtures("driver")
class TestRegisterNewAccount:

    # Успешная регистрация используя randomizer
    def test_registration_success(self, driver):
        user_name = generate_name()
        user_email = generate_email()
        user_password = generate_password()

        driver.find_element(*Locators.login_button_main_page).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.register_link))

        driver.find_element(*Locators.register_link).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.register_button))

        driver.find_element(*Locators.field_name).send_keys(user_name)
        driver.find_element(*Locators.field_email).send_keys(user_email)
        driver.find_element(*Locators.password_field).send_keys(user_password)
        driver.find_element(*Locators.register_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.login_button))

        assert driver.find_element(*Locators.login_button).is_displayed()
