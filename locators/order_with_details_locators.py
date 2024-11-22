from selenium.webdriver.common.by import By


class OrderWithDetailsLocators:
    ORDER_LIST = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"][text()="Лента Заказов"]')
    ORDER_LIST_TEXT = (By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"][text()="Лента заказов"]')
    FIRST_LIST_ORDER = ((By.XPATH, '(//h2[@class="text text_type_main-medium mb-2"])[1]'))
    COMPOSITION_TEXT = (By.XPATH, '//p[@class ="text text_type_main-medium mb-8"][text()="Cостав"]')
