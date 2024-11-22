import allure
from locators.main_functionality_locators import MainFunctionalityLocators
from page.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class MainFunctionalityPage(BasePage):
    @allure.step('Переход по клику на «Личный кабинет»')
    def click_to_personal_account(self):
        self.click_to_element(MainFunctionalityLocators.PERSONAL_ACCOUNT)

    @allure.step('Авторизоваться')
    def enter_email_password(self, email, password):
        self.get_text_from_element(MainFunctionalityLocators.ENTRANCE_TEXT)
        self.add_text_to_element(MainFunctionalityLocators.LOGIN_EMAIL, email)
        self.add_text_to_element(MainFunctionalityLocators.LOGIN_PASSWORD, password)
        self.click_to_element(MainFunctionalityLocators.LOGIN_ACCOUNT)

    @allure.step('Проверяем, что на главной странице')
    def verification_main_page(self):
        self.find_element_with_wait(MainFunctionalityLocators.YOUR_ORDER)

    @allure.step('Переход по клику на «Конструктор»')
    def click_to_constructor(self):
        self.click_to_element(MainFunctionalityLocators.CONSTRUCTOR_TEXT)
        self.find_element_with_wait(MainFunctionalityLocators.BUN_XPATH)

    @allure.step('Переход по клику на «Лента заказов»')
    def click_to_order_list(self):
        self.click_to_element(MainFunctionalityLocators.ORDER_LIST)
        self.find_element_with_wait(MainFunctionalityLocators.ORDER_LIST_TEXT)

    @allure.step('Кликнуть на ингредиент, появится всплывающее окно с деталями')
    def click_to_ingredient(self):
        self.click_to_element(MainFunctionalityLocators.CONSTRUCTOR_TEXT)
        self.find_element_with_wait(MainFunctionalityLocators.BUN_XPATH)
        self.click_to_element(MainFunctionalityLocators.INGREDIENT_XPATH)
        self.find_element_with_wait(MainFunctionalityLocators.INGREDIENT_DETAILS)

    @allure.step('Кликнуть по крестику, всплывающее окно закрывается ')
    def click_to_cross(self):
        self.click_to_element(MainFunctionalityLocators.CROSS_XPATH)
        self.find_element_with_wait(MainFunctionalityLocators.BUN_XPATH)

    @allure.step('Добавляем ингредиент, каунтер данного ингредиента увеличивается')
    def add_ingredient(self):
        ingredient_element = self.find_element_with_wait(MainFunctionalityLocators.INGREDIENT_XPATH)
        basket_element = self.find_element_with_wait(MainFunctionalityLocators.BASKET_LIST)
        action = ActionChains(self.driver)
        action.drag_and_drop(ingredient_element, basket_element).perform()
        self.find_element_with_wait(MainFunctionalityLocators.COUNTER_NUM)

    @allure.step('Проверяем, что залогиненный пользователь может оформить заказ')
    def verification_place_order(self):
        self.click_to_element(MainFunctionalityLocators.YOUR_ORDER)
        status_text = self.get_text_from_element(MainFunctionalityLocators.COOKING_ORDER)
        return status_text









