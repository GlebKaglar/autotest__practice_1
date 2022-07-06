import time

from auto_site.autotest_practice_1.Site1.base.seleniumbase import SeleniumBase
from auto_site.autotest_practice_1.Site1.pom.locators import HomePageLocators


class HomepageWishList(SeleniumBase):

    def should_be_wishlist_icon(self):
        print('\tПроверяем наличие кнопки поиска')
        assert self.is_element_present(*HomePageLocators.WISHLIST_ELEMENT), 'Wishlist element not found'
        time.sleep(2)

    def go_to_wishlist(self):
        print('\tПереходим в панель избранного')
        wishlist_el = self.driver.find_element(*HomePageLocators.WISHLIST_ELEMENT)
        wishlist_el.click()
        time.sleep(2)

    def go_to_catalog(self):
        print('\tПереходим в каталог')
        assert self.is_element_present(*HomePageLocators.WISHLIST_GO_TO_CAT), 'WISHLIST_GO_TO_CAT not found'
        button_to_cat = self.driver.find_element(*HomePageLocators.WISHLIST_GO_TO_CAT)
        button_to_cat.click()
        url_substring = 'all-product-cat'
        current_url = self.driver.current_url
        assert url_substring in current_url, 'INVALID URL'
        print('\tСсылка верна')
        time.sleep(2)

    def close_wishlist(self):
        print('\tЗакрываем вишлист')
        assert self.is_element_present(*HomePageLocators.WISHLIST_CLOSE), 'WISHLIST_CLOSE not found'
        close_button = self.driver.find_element(*HomePageLocators.WISHLIST_CLOSE)
        close_button.click()
        time.sleep(2)

    def delete_product(self):
        print('\tУдаляем товар из избранного')
        assert self.is_element_present(*HomePageLocators.WISHLIST_UNHEART), 'WISHLIST_UNHEART not found'
        unheart = self.driver.find_element(*HomePageLocators.WISHLIST_UNHEART)
        unheart.click()
        delete = self.driver.find_element(*HomePageLocators.WISHLIST_DELETE)
        delete.click()