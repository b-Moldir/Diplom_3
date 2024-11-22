from selenium.webdriver.common.by import By


class MainFunctionalityLocators:
    PERSONAL_ACCOUNT = (By.XPATH, '//header[@class="AppHeader_header__X9aJA pb-4 pt-4"]//p[text()="Личный Кабинет"]')
    LOGIN_EMAIL = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    LOGIN_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')
    LOGIN_ACCOUNT = (By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//button[text()="Войти"]')
    YOUR_ORDER= (By.XPATH, '//section[2]//button[text()="Оформить заказ"]')
    CONSTRUCTOR_TEXT = (By.XPATH, '//header[@class="AppHeader_header__X9aJA pb-4 pt-4"]//p[text()="Конструктор"]')
    BUN_XPATH = (By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//span[text()="Булки"]')
    ORDER_LIST = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"][text()="Лента Заказов"]')
    ORDER_LIST_TEXT = (By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"][text()="Лента заказов"]')
    INGREDIENT_XPATH = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    INGREDIENT_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CROSS_XPATH = (By.CSS_SELECTOR, '.Modal_modal_opened__3ISw4 > div:nth-child(1) > button:nth-child(2) > svg:nth-child(1) > path:nth-child(1)')
    BASKET_LIST = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    COUNTER_NUM = (By.XPATH, '//p[@class="counter_counter__num__3nue1"][text()=2]')
    COOKING_ORDER = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    ENTRANCE_TEXT = (By.XPATH, '//*[@id="root"]/div/main/div/h2')


