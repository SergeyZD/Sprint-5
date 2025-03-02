from selenium.webdriver.common.by import By


class Locators:
    # Кнопка "Личный кабинет"
    my_account_button = By.XPATH, '//p[text() = "Личный Кабинет"]'

    # Кнопка "Войти в аккаунт" на главной странице
    login_button_main_page = (By.XPATH, './/button[text() = "Войти в аккаунт"]')

    # Кнопка "Зарегистрироваться"
    register_button = (By.XPATH, '//button[text() = "Зарегистрироваться"]')

    # Ссылка "Зарегистрироваться"
    register_link = (By.XPATH, '//a[text() = "Зарегистрироваться"]')

    # Поле "Имя"
    field_name = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")

    # Поле "Email"
    field_email = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")

    # Поле "Пароль"
    password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")

    # Кнопка "Войти"
    login_button = (By.XPATH, './/button[text()="Войти"]')

    # Кнопка "Войти" на форме регистрации
    login_button_in_registration_form = By.XPATH, '//a[text() = "Войти"]'

    # Сообщение об ошибке "Некорректный пароль"
    incorrect_password_message = By.XPATH, '//p[text() = "Некорректный пароль"]'

    # Кнопка "Оформить заказ"
    make_order_button = By.XPATH, '//button[text()="Оформить заказ"]'

    # Кнопка "Восстановить пароль"
    forgot_password_button = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Кнопка "Войти" в форме восстановления пароля
    login_button_in_password_recovery_form = By.XPATH, '//a[text() = "Войти"]'

    # Раздел "Профиль"
    profile = By.XPATH, '//a[@href = "/account/profile"]'

    # Раздел "История заказов"
    order_history = By.XPATH, '//a[@href = "/account/order-history"]'

    # Кнопка "Конструктор"
    constructor_button = By.XPATH, '//p[text() = "Конструктор"]'

    # Лого в шапке сайта
    logo_in_header = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'

    # Кнопка "Выйти"
    exit_button = By.XPATH, '//button[text()="Выход"]'

    # Заголовок раздела "Булки"
    buns_section = By.XPATH, '//span[text() = "Булки"]'

    # Заголовок раздела "Соусы"
    sauces_section = By.XPATH, '//span[text() = "Соусы"]'

    # Заголовок раздела "Начинки"
    ingredients_section = By.XPATH, '//span[text() = "Начинки"]'

    # Активный раздел конструктора
    selected_section = (
        By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')
