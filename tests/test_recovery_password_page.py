import allure
from page.recovery_password_page import RecoveryPasswordPage
from data import EMAIL


class TestRecoveryPasswordPage:
    @allure.title('Проверка в окне Восстановление пароля')
    @allure.description(
        'Проверяем, что при клике по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_recovery_password(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.click_to_personal_account()
        recovery_password_page.verification_personal_account()
        recovery_password_page.click_to_recovery_password()
        recovery_password_page.verification_recovery_password()
        recovery_password_page.add_email(EMAIL)
        recovery_password_page.click_to_recovery()
        recovery_password_page.verification_recovery_password_2()
        recovery_password_page.click_to_icon_password()

        assert recovery_password_page.password_field_highlighted() == True

