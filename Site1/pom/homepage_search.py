import time

from auto_site.autotest_practice_1.Site1.base.seleniumbase import SeleniumBase
from auto_site.autotest_practice_1.Site1.pom.locators import HomePageLocators


class HomepageSearch(SeleniumBase):

    def should_be_search_icon(self):
        print('\tПроверяем наличие кнопки поиска')
        assert self.is_element_present(*HomePageLocators.SEARCH_ELEMENT), 'Search element not found'
        time.sleep(2)

    def go_to_search(self):
        print('\tНажимаем на кнопку поиска')
        search_icon = self.driver.find_element(*HomePageLocators.SEARCH_ELEMENT)
        search_icon.click()
        time.sleep(2)

    def send_keys_to_search(self):
        print('\tВводим поисковый запрос и ищем')
        assert self.is_element_present(*HomePageLocators.SEARCH_FIELD), 'Search field not found'
        search_field = self.driver.find_element(*HomePageLocators.SEARCH_FIELD)
        search_field.send_keys('Рюкзак')
        assert self.is_element_present(*HomePageLocators.SEARCH_BTN), 'Search button not found'
        search_btn = self.driver.find_element(*HomePageLocators.SEARCH_BTN)
        search_btn.click()
        time.sleep(2)

    def search_close(self):
        print('\tЗакрываем строку поиска')
        assert self.is_element_present(*HomePageLocators.SEARCH_CLOSE_BTN), 'Close button not found'
        search_close_btn = self.driver.find_element(*HomePageLocators.SEARCH_CLOSE_BTN)
        search_close_btn.click()
        time.sleep(2)
