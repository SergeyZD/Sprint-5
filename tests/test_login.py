import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con
from helpers.locators import Locators


@pytest.mark.usefixtures("credentials", "driver")
class TestLogin:

    # Вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_via_main_page(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.login_button_main_page).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.login_button))
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.make_order_button))

        assert driver.find_element(*Locators.make_order_button).is_displayed()

    # Вход через «Личный кабинет»
    def test_login_via_my_account(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.my_account_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.login_button))
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.make_order_button))

        assert driver.find_element(*Locators.make_order_button).is_displayed()

    # Вход через кнопку «Войти» в форме регистрации
    def test_login_via_registration_form(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.login_button_main_page).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.register_link))
        driver.find_element(*Locators.register_link).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.register_button))
        driver.find_element(*Locators.login_button_in_registration_form).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.make_order_button))

        assert driver.find_element(*Locators.make_order_button).is_displayed()

    # Вход через кнопку «Войти» в форме восстановления пароля
    def test_login_via_password_recovery(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.my_account_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.register_link))
        driver.find_element(*Locators.forgot_password_button).click()
        WebDriverWait(driver, 5).until(
            exp_con.visibility_of_element_located(Locators.login_button_in_password_recovery_form))
        driver.find_element(*Locators.login_button_in_password_recovery_form).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.login_button))
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.make_order_button))

        assert driver.find_element(*Locators.make_order_button).is_displayed()
