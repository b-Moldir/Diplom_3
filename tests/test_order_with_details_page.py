import allure
from page.order_with_details_page import OrderWithDetailsPage

class TestOrderWithDetailsPage:
    @allure.title('Проверка всплывающего окна с деталями')
    @allure.description('Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_with_details(self, driver):
        order_with_details_page = OrderWithDetailsPage(driver)
        order_with_details_page.click_to_order_list()
        order_with_details_page.click_to_order()

        assert order_with_details_page.verification_order_with_details() == "Cостав"
