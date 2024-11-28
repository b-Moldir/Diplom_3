import allure
from page.counter_all_time_page import CounterAllTimePage

class TestCounterAllTimePage():
    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Проверяем, что после создания нового заказа счетчик Выполнено за всё время увеличивается')
    def test_counter_all_time(self, user_data, driver):
        email, password = user_data
        counter_all_time_page = CounterAllTimePage(driver)
        counter_all_time_page.click_to_personal_account()
        counter_all_time_page.enter_email_password(email, password)
        counter_all_time_page.verification_main_page()
        all_time_counter = counter_all_time_page.click_to_order_list()
        counter_all_time_page.click_to_constructor()
        counter_all_time_page.add_ingredient()
        counter_all_time_page.click_to_place_an_order()
        all_time_counter_1 = counter_all_time_page.verification_counter_all_time()

        assert all_time_counter_1 > all_time_counter
