from selenium.webdriver.common.by import By


class SectionAtWorkLocators:
    PERSONAL_ACCOUNT = (By.XPATH, '//header[@class="AppHeader_header__X9aJA pb-4 pt-4"]//p[text()="Личный Кабинет"]')
    LOGIN_EMAIL = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    LOGIN_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')
    LOGIN_ACCOUNT = (By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//button[text()="Войти"]')
    ENTRANCE_TEXT = (By.XPATH, '//*[@id="root"]/div/main/div/h2')
    YOUR_ORDER = (By.XPATH, '//section[2]//button[text()="Оформить заказ"]')
    INGREDIENT_XPATH = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    BASKET_LIST = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    CROSS_BUTTON = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    COUNTER_NUM = (By.XPATH, '//p[@class="counter_counter__num__3nue1"][text()=2]')
    COOKING_ORDER = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    ORDER_LIST = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"][text()="Лента Заказов"]')
    ORDER_LIST_TEXT = (By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"][text()="Лента заказов"]')
    AT_WORK_XPATH = (By.XPATH, '//ul[2]/li[1][@class="text text_type_digits-default mb-2"]')
    IDENTIFIER_ORDER = (By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')