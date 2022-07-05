from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def __get_selenium_by(self, find_by: str) -> dict:
        # Возвращает словарь
        # добавили __ в начало класса, чтобы метод был приватным и работал исключительно в этом классе
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'tag_name': By.TAG_NAME,
                    'name': By.NAME,
                    'link_text': By.LINK_TEXT,
                    'partial_link_text': By.PARTIAL_LINK_TEXT
                    }
        return locating[find_by]

    # Ждем и возвращаем WebElement, когда элемент будет виден
    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    # Ждем и возвращаем WebElement, если он присутсвует в DOM
    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Ждем, пока элемент не исчезнет
    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    # Ждем и возвращаем WebElement (список), когда элементы будут видны
    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(EC.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    # Ждем и возвращаем WebElement (список), если он присутсвуют в DOM
    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(EC.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    # Получаем список с текстом WebElement
    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]

     # Получаем WebElement по тексту в нем
    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]