import allure
from page.recovery_password_page import RecoveryPasswordPage
from data import EMAIL


class TestRecoveryPasswordPage:
    @allure.title('Проверка в окне Восстановление пароля')
    @allure.description(
        'Проверяем, что при клике по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_recovery_password(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.add_email(EMAIL)

        assert recovery_password_page.password_field_highlighted()


