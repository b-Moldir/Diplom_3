import allure
from locators.order_with_details_locators import OrderWithDetailsLocators
from page.base_page import BasePage


class OrderWithDetailsPage(BasePage):
    @allure.step('Переход по клику на «Лента заказов»')
    def click_to_order_list(self):
        self.move_to_element_and_click(OrderWithDetailsLocators.ORDER_LIST)
        self.find_element_with_wait(OrderWithDetailsLocators.ORDER_LIST_TEXT)

    @allure.step('Кликнуть на заказ')
    def click_to_order(self):
        self.click_to_element(OrderWithDetailsLocators.FIRST_LIST_ORDER)

    @allure.step('Проверяем, что открывается всплывающее окно с деталями')
    def verification_order_with_details(self):
        composition_text = self.get_text_from_element(OrderWithDetailsLocators.COMPOSITION_TEXT)
        return composition_text





