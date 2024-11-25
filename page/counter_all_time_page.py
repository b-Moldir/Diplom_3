import allure
from locators.counter_all_time_locators import CounterAllTimeLocators
from page.base_page import BasePage


class CounterAllTimePage(BasePage):
    @allure.step('Переход по клику на «Личный кабинет»')
    def click_to_personal_account(self):
        self.click_to_element(CounterAllTimeLocators.PERSONAL_ACCOUNT)

    @allure.step('Авторизоваться')
    def enter_email_password(self, email, password):
        self.get_text_from_element(CounterAllTimeLocators.ENTRANCE_TEXT)
        self.add_text_to_element(CounterAllTimeLocators.LOGIN_EMAIL, email)
        self.add_text_to_element(CounterAllTimeLocators.LOGIN_PASSWORD, password)
        self.click_to_element(CounterAllTimeLocators.LOGIN_ACCOUNT)

    @allure.step('Проверяем, что на главной странице')
    def verification_main_page(self):
        self.find_element_with_wait(CounterAllTimeLocators.YOUR_ORDER)

    @allure.step('Переход по клику на «Лента заказов»')
    def click_to_order_list(self):
        self.move_to_element_and_click(CounterAllTimeLocators.ORDER_LIST)
        self.find_element_with_wait(CounterAllTimeLocators.ORDER_LIST_TEXT)
        all_time_counter = self.get_text_from_element(CounterAllTimeLocators.ALL_TIME_XPATH)
        return all_time_counter

    @allure.step('Переход по клику на «Конструктор»')
    def click_to_constructor(self):
        self.move_to_element_and_click(CounterAllTimeLocators.CONSTRUCTOR_TEXT)
        self.find_element_with_wait(CounterAllTimeLocators.BUN_XPATH)

    @allure.step('Добавляем ингредиент, каунтер данного ингредиента увеличивается')
    def add_ingredient(self):
        self.drag_and_drop_element(CounterAllTimeLocators.INGREDIENT_XPATH, CounterAllTimeLocators.BASKET_LIST)
        self.find_element_with_wait(CounterAllTimeLocators.COUNTER_NUM)

    @allure.step('Кликаем на кнопку "Оформить заказ"')
    def click_to_place_an_order(self):
        self.move_to_element_and_click(CounterAllTimeLocators.YOUR_ORDER)
        self.get_text_from_element(CounterAllTimeLocators.COOKING_ORDER)
        self.click(CounterAllTimeLocators.CROSS_BUTTON)
        self.find_element_with_wait(CounterAllTimeLocators.YOUR_ORDER)

    @allure.step('Проверяем, при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def verification_counter_all_time(self):
        self.click(CounterAllTimeLocators.ORDER_LIST)
        self.find_element_with_wait(CounterAllTimeLocators.ORDER_LIST_TEXT)
        all_time_counter_1 = self.get_text_from_element(CounterAllTimeLocators.ALL_TIME_XPATH)
        return all_time_counter_1
