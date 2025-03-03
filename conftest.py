import pytest

from selenium import webdriver
from helpers.urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.burger_url_main)
    yield driver
    driver.quit()


@pytest.fixture
def credentials():
    return {
        "email": "Sergeyzdanovich15111@yandex.ru",
        "password": "123456"
    }