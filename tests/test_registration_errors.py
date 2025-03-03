import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con
from helpers.randomizer import generate_name, generate_email, generate_password, generate_incorrect_password
from helpers.locators import Locators


@pytest.mark.usefixtures("driver")
class TestRegisterErrors:

    # Ошибка для невалидного пароля
    def test_registration_incorrect_password_message(self, driver):
        user_name = generate_name()
        user_email = generate_email()
        user_password = generate_password()
        not_user_password = generate_incorrect_password()

        driver.find_element(*Locators.login_button_main_page).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.register_link))

        driver.find_element(*Locators.register_link).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.register_button))

        driver.find_element(*Locators.field_name).send_keys(user_name)
        driver.find_element(*Locators.field_email).send_keys(user_email)
        driver.find_element(*Locators.password_field).send_keys(user_password)
        driver.find_element(*Locators.register_button).click()

        WebDriverWait(driver, 10).until(exp_con.visibility_of_element_located(Locators.login_button))
        driver.find_element(*Locators.login_button).click()

        driver.find_element(*Locators.field_email).send_keys(user_name)
        driver.find_element(*Locators.password_field).send_keys(not_user_password)
        driver.find_element(*Locators.login_button).click()

        WebDriverWait(driver, 5).until(exp_con.presence_of_element_located(Locators.incorrect_password_message))

        assert driver.find_element(*Locators.incorrect_password_message).text == 'Некорректный пароль'
