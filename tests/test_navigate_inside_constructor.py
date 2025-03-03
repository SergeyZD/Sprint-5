import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con
from helpers.locators import Locators


@pytest.mark.usefixtures("credentials", "driver")
class TestNavigateInsideConstructor:

    # Переход из раздела "Соусы" в раздел "Булки"
    def test_navigate_sauces_to_buns(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.make_order_button))
        driver.find_element(*Locators.sauces_section).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.buns_section))
        driver.find_element(*Locators.buns_section).click()

        assert driver.find_element(*Locators.selected_section).text == "Булки"


    # Переход из раздела "Начинки" в раздел "Соусы"
    def test_navigate_ingredients_to_sauces(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.make_order_button))
        driver.find_element(*Locators.ingredients_section).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.sauces_section))
        driver.find_element(*Locators.sauces_section).click()

        assert driver.find_element(*Locators.selected_section).text == "Соусы"


    # Переход из раздела "Cоусы" в раздел "Начинки"
    def test_navigate_buns_to_ingredients(self, credentials, driver):
        email = credentials["email"]
        password = credentials["password"]

        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.sauces_section))
        driver.find_element(*Locators.sauces_section).click()
        WebDriverWait(driver, 5).until(exp_con.visibility_of_element_located(Locators.make_order_button))
        driver.find_element(*Locators.ingredients_section).click()

        assert driver.find_element(*Locators.selected_section).text == "Начинки"
