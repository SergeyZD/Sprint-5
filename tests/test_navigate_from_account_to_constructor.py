import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con
from helpers.locators import Locators


@pytest.mark.usefixtures("credentials", "driver")
class TestNavigateFromAccountToConstructor:

    # Переход по клику на «Конструктор»
    def test_navigate_from_account_to_constructor_via_button(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.my_account_button))
        driver.find_element(*Locators.my_account_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.constructor_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.make_order_button))

        assert driver.find_element(*Locators.make_order_button).is_displayed()

    # Переход по клику на логотип Stellar Burgers
    def test_navigate_from_account_to_constructor_via_logo(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.my_account_button))
        driver.find_element(*Locators.my_account_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.logo_in_header).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.make_order_button))

        assert driver.find_element(*Locators.make_order_button).is_displayed()
