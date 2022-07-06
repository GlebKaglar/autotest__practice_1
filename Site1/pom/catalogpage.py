from selenium.webdriver.common.by import By

from auto_site.autotest_practice_1.Site1.base.seleniumbase import SeleniumBase


class CatalogPage(SeleniumBase):
    def add_product_to_wishlist(self):
        print('\tДобавляем товар в вишлист')
        self.driver.find_element(By.CLASS_NAME, 'a8').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-title="OS"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > .cli__prod--heart').click()
