import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con
from helpers.locators import Locators


@pytest.mark.usefixtures("credentials", "driver")
class TestLogout:

    # Выход по кнопке «Выйти» в личном кабинете
    def test_logout(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.my_account_button))
        driver.find_element(*Locators.my_account_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.exit_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.login_button))

        assert driver.find_element(*Locators.login_button).is_displayed()
