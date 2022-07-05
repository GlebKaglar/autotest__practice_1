import time

from auto_site.autotest_practice_1.Site1.base.seleniumbase import SeleniumBase
from auto_site.autotest_practice_1.Site1.pom.locators import HomePageLocators


class HomepageSearch(SeleniumBase):

    def should_be_search_icon(self):
        print('Проверяем наличие кнопки поиска')
        self.is_element_present(*HomePageLocators.SEARCH_ICON)
        time.sleep(2)

    def go_to_search(self):
        print('Нажимаем на кнопку поиска')
        search_icon = self.driver.find_element(*HomePageLocators.SEARCH_ICON)
        search_icon.click()
        time.sleep(2)

    def send_keys_to_search(self):
        print('Вводим поисковый запрос и ищем')
        search_field = self.driver.find_element(*HomePageLocators.SEARCH_FIELD)
        search_field.send_keys('Рюкзак')
        search_btn = self.driver.find_element(*HomePageLocators.SEARCH_BTN)
        search_btn.click()
        time.sleep(2)
