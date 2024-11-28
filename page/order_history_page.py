import allure
from locators.order_history_locators import OrderHistoryLocators
from page.base_page import BasePage


class OrderHistoryPage(BasePage):
    @allure.step('Переход по клику на «Личный кабинет»')
    def click_to_personal_account(self):
        self.click_to_element(OrderHistoryLocators.PERSONAL_ACCOUNT)

    @allure.step('Авторизоваться')
    def enter_email_password(self, email, password):
        self.get_text_from_element(OrderHistoryLocators.ENTRANCE_TEXT)
        self.add_text_to_element(OrderHistoryLocators.LOGIN_EMAIL, email)
        self.add_text_to_element(OrderHistoryLocators.LOGIN_PASSWORD, password)
        self.click_to_element(OrderHistoryLocators.LOGIN_ACCOUNT)

    @allure.step('Проверяем, что на главной странице')
    def verification_main_page(self):
        self.find_element_with_wait(OrderHistoryLocators.YOUR_ORDER)

    @allure.step('Добавляем ингредиент, каунтер данного ингредиента увеличивается')
    def add_ingredient(self):
        self.drag_and_drop_element(OrderHistoryLocators.INGREDIENT_XPATH, OrderHistoryLocators.BASKET_LIST)
        self.find_element_with_wait(OrderHistoryLocators.COUNTER_NUM)

    @allure.step('Кликаем на кнопку "Оформить заказ"')
    def click_to_place_an_order(self):
        self.move_to_element_and_click(OrderHistoryLocators.YOUR_ORDER)
        self.get_text_from_element(OrderHistoryLocators.COOKING_ORDER)
        self.click(OrderHistoryLocators.CROSS_BUTTON)
        self.find_element_with_wait(OrderHistoryLocators.YOUR_ORDER)

    @allure.step('Переход по клику на «Личный кабинет»')
    def click_to_personal_account_1(self):
        self.click(OrderHistoryLocators.PERSONAL_ACCOUNT)
        self.get_text_from_element(OrderHistoryLocators.PROFILE_TEXT)

    @allure.step('Проверяем, заказ из раздела «История заказов» отображаются на странице «Лента заказов»')
    def verification_display_order(self):
        self.click(OrderHistoryLocators.ORDER_HISTORY_BUTTON)
        order_number_locator = OrderHistoryLocators.ORDER_HISTORY_IN_HISTORY
        order_number = self.get_text_from_element(order_number_locator)
        self.click_to_element(OrderHistoryLocators.ORDER_LIST)
        self.find_element_with_wait(OrderHistoryLocators.ORDER_LIST_TEXT)
        self.scroll_until_the_last(OrderHistoryLocators.ORDER_HISTORY_IN_HISTORY)
        order_number_1 = self.get_text_from_element(order_number_locator)
        return order_number, order_number_1







