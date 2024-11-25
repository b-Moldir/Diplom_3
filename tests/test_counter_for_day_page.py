import allure
from page.counter_for_day_page import CounterForDaysPage

class TestCounterForDayPage():
    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Проверяем, что после создания нового заказа счетчик Выполнено за сегодня увеличивается')
    def test_counter_for_day(self, user_data, driver):
        email, password = user_data
        counter_for_day_page = CounterForDaysPage(driver)
        counter_for_day_page.click_to_personal_account()
        counter_for_day_page.enter_email_password(email, password)
        counter_for_day_page.verification_main_page()
        for_day_counter = counter_for_day_page.click_to_order_list()
        counter_for_day_page.click_to_constructor()
        counter_for_day_page.add_ingredient()
        counter_for_day_page.click_to_place_an_order()
        for_day_counter_1 = counter_for_day_page.verification_counter_for_day()

        assert for_day_counter_1 > for_day_counter
