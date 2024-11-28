import allure
from page.main_functionality_page import MainFunctionalityPage


class TestMainFunctionalityPage:
    @allure.title('Проверка основного функционала')
    @allure.description('Проверяем, что залогиненный пользователь может оформить заказ')
    def test_main_functional(self, user_data, driver):
        email, password = user_data
        main_functional_page = MainFunctionalityPage(driver)
        main_functional_page.click_to_personal_account()
        main_functional_page.enter_email_password(email, password)
        main_functional_page.verification_main_page()
        main_functional_page.click_to_constructor()
        main_functional_page.click_to_order_list()
        main_functional_page.click_to_ingredient()
        main_functional_page.click_to_cross()
        main_functional_page.add_ingredient()

        assert main_functional_page.verification_place_order() == "Ваш заказ начали готовить"

