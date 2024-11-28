from selenium.webdriver.common.by import By


class RecoveryPasswordLocators:
    PERSONAL_ACCOUNT = (By.XPATH, '//header[@class="AppHeader_header__X9aJA pb-4 pt-4"]//p[text()="Личный Кабинет"]')
    FORGOT_PASSWORD_TEXT = (By.XPATH, '//main//p[2][text()="Забыли пароль?"]')
    RECOVER_PASSWORD = (By.CSS_SELECTOR, 'p:nth-child(2) > a')
    RECOVERY_PASSWORD_TEXT = (By.XPATH, '//main//h2[text()="Восстановление пароля"]')
    LOGIN_EMAIL = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    BUTTON_RESTORE = (By.XPATH, '//button[text()="Восстановить"]')
    ICON_LOCATOR = (By.CSS_SELECTOR, '.input__icon > svg:nth-child(1) > path')
    FIELD_PASSWORD_LOCATOR = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div')
    LABEL_PASSWORD_LOCATOR = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/label')
