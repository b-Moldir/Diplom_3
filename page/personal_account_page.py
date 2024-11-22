import allure
from page.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccountPage(BasePage):
    @allure.step('Переход по клику на «Личный кабинет»')
    def click_to_personal_account(self):
        self.click_to_element(PersonalAccountLocators.PERSONAL_ACCOUNT)

    @allure.step('Авторизоваться')
    def enter_email_password(self, email, password):
        self.get_text_from_element(PersonalAccountLocators.ENTRANCE_TEXT)
        self.add_text_to_element(PersonalAccountLocators.LOGIN_EMAIL, email)
        self.add_text_to_element(PersonalAccountLocators.LOGIN_PASSWORD, password)
        self.click_to_element(PersonalAccountLocators.LOGIN_ACCOUNT)

    @allure.step('Проверяем, что на главной странице')
    def verification_main_page(self):
        self.find_element_with_wait(PersonalAccountLocators.YOUR_ORDER)

    @allure.step('Переход по клику на «Личный кабинет»')
    def click_to_personal_account_1(self):
        self.click_to_element(PersonalAccountLocators.PERSONAL_ACCOUNT)
        self.get_text_from_element(PersonalAccountLocators.PROFILE_TEXT)

    @allure.step('Переход в раздел «История заказов»')
    def click_to_history_button(self):
        self.click_to_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Выход из аккаунта')
    def click_to_exit_button(self):
        self.click_to_element(PersonalAccountLocators.EXIT_BUTTON)

    @allure.step('Проверяем, что вышли из аккаунта')
    def verification_logged_out_account(self):
        account_status_text = self.get_text_from_element(PersonalAccountLocators.ENTRANCE_TEXT)
        return account_status_text











