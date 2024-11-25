import allure
from page.section_at_work_page import SectionAtWorkPage

class TestSectionAtWorkPage():
    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе В работе')
    @allure.description('Проверяем, что после оформления заказа его номер появляется в разделе В работе')
    def test_section_at_work(self, user_data, driver):
        email, password = user_data
        section_at_work_page = SectionAtWorkPage(driver)
        section_at_work_page.click_to_personal_account()
        section_at_work_page.enter_email_password(email, password)
        section_at_work_page.verification_main_page()
        section_at_work_page.add_ingredient()
        order_number = section_at_work_page.click_to_place_an_order()
        order_number_1 = section_at_work_page.verification_order_number()

        assert int(order_number_1) == int(order_number)