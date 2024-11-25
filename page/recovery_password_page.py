import allure
from page.base_page import BasePage
from locators.recovery_password_locators import RecoveryPasswordLocators


class RecoveryPasswordPage(BasePage):
    @allure.step('Переход по клику на «Личный кабинет»')
    def click_to_personal_account(self):
        self.click(RecoveryPasswordLocators.PERSONAL_ACCOUNT)

    @allure.step('Проверяем, что в окне Личный кабинет')
    def verification_personal_account(self):
        self.get_text_from_element(RecoveryPasswordLocators.FORGOT_PASSWORD_TEXT)

    @allure.step('Кликнуть по кнопке Восстановить пароль')
    def click_to_recovery_password(self):
        self.click_to_element(RecoveryPasswordLocators.RECOVER_PASSWORD)

    @allure.step('Проверяем, что в окне Восстановление пароля')
    def verification_recovery_password(self):
        self.get_text_from_element(RecoveryPasswordLocators.RECOVERY_PASSWORD_TEXT)

    @allure.step('Ввести в поле емайл')
    def add_email(self, email):
        self.add_text_to_element(RecoveryPasswordLocators.LOGIN_EMAIL, email)

    @allure.step('Кликнуть по кнопке Восстановить')
    def click_to_recovery(self):
        self.click_to_element(RecoveryPasswordLocators.BUTTON_RESTORE)

    @allure.step('Проверяем, что в окне Восстановление пароля')
    def verification_recovery_password_2(self):
        self.get_text_from_element(RecoveryPasswordLocators.RECOVERY_PASSWORD_TEXT)

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_to_icon_password(self):
        self.click_to_element(RecoveryPasswordLocators.ICON_LOCATOR)

    @allure.step('Проверяем, после клика что поле активное — подсвечивает его')
    def password_field_highlighted(self):
        field = self.find_element_with_wait(RecoveryPasswordLocators.FIELD_PASSWORD_LOCATOR)
        label = self.find_element_with_wait(RecoveryPasswordLocators.LABEL_PASSWORD_LOCATOR)
        field_class = field.get_attribute("class")
        label_class = label.get_attribute("class")
        return "input_status_active" in field_class and "input__placeholder-focused" in label_class










