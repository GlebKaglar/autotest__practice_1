from selenium.webdriver.remote.webelement import WebElement
from typing import List
from auto_site.autotest_practice_1.Site1.base.seleniumbase import SeleniumBase


class HomepageNav(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '.sidebar__block.categories > a'  # локатор всех элементов на навигационной панели
        self.NAV_LINK_TEXT = 'АКСЕССУАРЫ,ЖЕНЩИНАМ,МУЖЧИНАМ,SALE'  # константа, для проверки

    def get_nav_links(self) -> List[WebElement]:  # Возвращает список веб-элементов
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:  # Из списка создаем строку
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        return ','.join(nav_links_text)
