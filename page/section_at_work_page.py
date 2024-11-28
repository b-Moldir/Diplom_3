import allure
from locators.section_at_work_locators import SectionAtWorkLocators
from page.base_page import BasePage
import time


class SectionAtWorkPage(BasePage):
    @allure.step('Переход по клику на «Личный кабинет»')
    def click_to_personal_account(self):
        self.click_to_element(SectionAtWorkLocators.PERSONAL_ACCOUNT)

    @allure.step('Авторизоваться')
    def enter_email_password(self, email, password):
        self.get_text_from_element(SectionAtWorkLocators.ENTRANCE_TEXT)
        self.add_text_to_element(SectionAtWorkLocators.LOGIN_EMAIL, email)
        self.add_text_to_element(SectionAtWorkLocators.LOGIN_PASSWORD, password)
        self.click_to_element(SectionAtWorkLocators.LOGIN_ACCOUNT)

    @allure.step('Проверяем, что на главной странице')
    def verification_main_page(self):
        self.find_element_with_wait(SectionAtWorkLocators.YOUR_ORDER)

    @allure.step('Добавляем ингредиент, каунтер данного ингредиента увеличивается')
    def add_ingredient(self):
        self.drag_and_drop_element(SectionAtWorkLocators.INGREDIENT_XPATH, SectionAtWorkLocators.BASKET_LIST)
        self.find_element_with_wait(SectionAtWorkLocators.COUNTER_NUM)

    @allure.step('Кликаем на кнопку "Оформить заказ"')
    def click_to_place_an_order(self):
        self.move_to_element_and_click(SectionAtWorkLocators.YOUR_ORDER)
        self.get_text_from_element(SectionAtWorkLocators.COOKING_ORDER)
        order_number_locator = SectionAtWorkLocators.IDENTIFIER_ORDER
        self.find_element_with_wait(order_number_locator)
        time.sleep(3)
        order_number = self.get_text_from_element(order_number_locator)
        print(order_number)
        self.click(SectionAtWorkLocators.CROSS_BUTTON)
        self.find_element_with_wait(SectionAtWorkLocators.YOUR_ORDER)
        return order_number

    @allure.step('Проверяем, при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def verification_order_number(self):
        self.click(SectionAtWorkLocators.ORDER_LIST)
        self.find_element_with_wait(SectionAtWorkLocators.ORDER_LIST_TEXT)
        order_number_1 = self.get_text_from_element(SectionAtWorkLocators.AT_WORK_XPATH)
        return order_number_1