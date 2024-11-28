from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    PERSONAL_ACCOUNT = (By.XPATH, '//header[@class="AppHeader_header__X9aJA pb-4 pt-4"]//p[text()="Личный Кабинет"]')
    LOGIN_EMAIL = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    LOGIN_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')
    LOGIN_ACCOUNT = (By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//button[text()="Войти"]')
    YOUR_ORDER= (By.XPATH, '//section[2]//button[text()="Оформить заказ"]')
    PROFILE_TEXT = (By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//a[text()="Профиль"]')
    ORDER_HISTORY_BUTTON = (By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//a[text()="История заказов"]')
    EXIT_BUTTON = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
    ENTRANCE_TEXT = (By.XPATH, '//*[@id="root"]/div/main/div/h2')