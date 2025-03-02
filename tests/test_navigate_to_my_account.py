import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con
from helpers.locators import Locators


@pytest.mark.usefixtures("credentials", "driver")
class TestNavigateToMyAccount:

    # Переход по клику на «Личный кабинет»
    def test_navigate_to_my_account_via_button(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.my_account_button).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.my_account_button))
        driver.find_element(*Locators.my_account_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.profile))

        assert driver.find_element(*Locators.order_history).is_displayed()
