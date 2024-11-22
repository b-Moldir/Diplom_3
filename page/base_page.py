from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.expected_url = None
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        element.click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def scroll_until_the_last(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 5).until(EC.visibility_of(element))

    def click(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def get_text_from_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return self.find_element_with_wait(locator).text

