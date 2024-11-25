import allure
from locators.counter_for_day_locators import CounterForDayLocators
from page.base_page import BasePage


class CounterForDaysPage(BasePage):
    @allure.step('Переход по клику на «Личный кабинет»')
    def click_to_personal_account(self):
        self.click_to_element(CounterForDayLocators.PERSONAL_ACCOUNT)

    @allure.step('Авторизоваться')
    def enter_email_password(self, email, password):
        self.get_text_from_element(CounterForDayLocators.ENTRANCE_TEXT)
        self.add_text_to_element(CounterForDayLocators.LOGIN_EMAIL, email)
        self.add_text_to_element(CounterForDayLocators.LOGIN_PASSWORD, password)
        self.click_to_element(CounterForDayLocators.LOGIN_ACCOUNT)

    @allure.step('Проверяем, что на главной странице')
    def verification_main_page(self):
        self.find_element_with_wait(CounterForDayLocators.YOUR_ORDER)

    @allure.step('Переход по клику на «Лента заказов»')
    def click_to_order_list(self):
        self.move_to_element_and_click(CounterForDayLocators.ORDER_LIST)
        self.find_element_with_wait(CounterForDayLocators.ORDER_LIST_TEXT)
        for_day_counter = self.get_text_from_element(CounterForDayLocators.FOR_DAY_XPATH)
        return for_day_counter

    @allure.step('Переход по клику на «Конструктор»')
    def click_to_constructor(self):
        self.move_to_element_and_click(CounterForDayLocators.CONSTRUCTOR_TEXT)
        self.find_element_with_wait(CounterForDayLocators.BUN_XPATH)

    @allure.step('Добавляем ингредиент, каунтер данного ингредиента увеличивается')
    def add_ingredient(self):
        self.drag_and_drop_element(CounterForDayLocators.INGREDIENT_XPATH, CounterForDayLocators.BASKET_LIST)
        self.find_element_with_wait(CounterForDayLocators.COUNTER_NUM)

    @allure.step('Кликаем на кнопку "Оформить заказ"')
    def click_to_place_an_order(self):
        self.move_to_element_and_click(CounterForDayLocators.YOUR_ORDER)
        self.get_text_from_element(CounterForDayLocators.COOKING_ORDER)
        self.click(CounterForDayLocators.CROSS_BUTTON)
        self.find_element_with_wait(CounterForDayLocators.YOUR_ORDER)

    @allure.step('Проверяем, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def verification_counter_for_day(self):
        self.click(CounterForDayLocators.ORDER_LIST)
        self.find_element_with_wait(CounterForDayLocators.ORDER_LIST_TEXT)
        for_day_counter_1 = self.get_text_from_element(CounterForDayLocators.FOR_DAY_XPATH)
        return for_day_counter_1

