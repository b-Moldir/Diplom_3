import allure
from page.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:
    @allure.title('Проверка в окне «Личный кабинет»')
    @allure.description('Проверяем, что выход из аккаунта')
    def test_personal_account(self, driver, user_data):
        email, password = user_data
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_to_personal_account()
        personal_account_page.enter_email_password(email, password)
        personal_account_page.verification_main_page()
        personal_account_page.click_to_personal_account_1()
        personal_account_page.click_to_history_button()
        personal_account_page.click_to_exit_button()

        assert personal_account_page.verification_logged_out_account() == "Вход"




