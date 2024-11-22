from selenium.webdriver.common.by import By


class OrderHistoryLocators:
    PERSONAL_ACCOUNT = (By.XPATH, '//header[@class="AppHeader_header__X9aJA pb-4 pt-4"]//p[text()="Личный Кабинет"]')
    LOGIN_EMAIL = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    LOGIN_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')
    LOGIN_ACCOUNT = (By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//button[text()="Войти"]')
    YOUR_ORDER = (By.XPATH, '//section[2]//button[text()="Оформить заказ"]')
    INGREDIENT_XPATH = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    BASKET_LIST = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    CROSS_BUTTON = (By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS > svg:nth-child(1) > path')
