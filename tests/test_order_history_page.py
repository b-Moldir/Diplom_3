import allure
from page.order_history_page import OrderHistoryPage


class TestHistoryOrderPage:
    @allure.title('Проверка заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Проверяем, что заказ из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_history(self, driver, user_data):
        email, password = user_data
        order_history_page = OrderHistoryPage(driver)
        order_history_page.click_to_personal_account()
        order_history_page.enter_email_password(email, password)
        order_history_page.verification_main_page()
        order_history_page.add_ingredient()
        order_history_page.click_to_place_an_order()
        order_history_page.click_to_personal_account_1()
        order_number, order_number_1 = order_history_page.verification_display_order()

        assert order_number == order_number_1


