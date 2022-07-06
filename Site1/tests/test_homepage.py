import time

import pytest

from auto_site.autotest_practice_1.Site1.pom.catalogpage import CatalogPage
from auto_site.autotest_practice_1.Site1.pom.homepage_nav import HomepageNav
from auto_site.autotest_practice_1.Site1.pom.homepage_search import HomepageSearch
from auto_site.autotest_practice_1.Site1.pom.homepage_wishlist import HomepageWishList


@pytest.mark.usefixtures('setup')
class TestHomepage:

    # Проверяем наличие (соответствие с NAV_LINK_TEXT) категорий навигационной панели
    def test_nav_links(self):
        print('Проверка соответствия категорий и переход по ним')
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Nav Link Text'
        # Проходим по всем категориям
        for index in range(4):
            homepage_nav.get_nav_links()[index].click()
            time.sleep(3)

    # Проверяем работу поисковой строки
    def test_search(self):
        print('Проверка поисковой строки')
        homepage_search = HomepageSearch(self.driver)
        homepage_search.should_be_search_icon()
        homepage_search.go_to_search()
        homepage_search.send_keys_to_search()
        homepage_search.search_close()

    # Проверяем переход из вишлиста в каталог товаров
    def test_wishlist_to_all_product_catalog(self):
        print('Проверка перехода из вишлиста в каталог')
        homepage_wishlist = HomepageWishList(self.driver)
        homepage_wishlist.should_be_wishlist_icon()
        homepage_wishlist.go_to_wishlist()
        homepage_wishlist.go_to_catalog()

    # Проверяем закрытие вишлиста
    def test_close_wishlist(self):
        print('Проверка закрытия вишлиста')
        homepage_wishlist = HomepageWishList(self.driver)
        homepage_wishlist.should_be_wishlist_icon()
        homepage_wishlist.go_to_wishlist()
        homepage_wishlist.close_wishlist()

    # Проверяем удаление товара из вишлиста
    def test_delete_product_from_wishlist(self):
        print('Проверка удаления продукта из вишлиста')
        homepage_wishlist = HomepageWishList(self.driver)
        homepage_wishlist.should_be_wishlist_icon()
        homepage_wishlist.go_to_wishlist()
        homepage_wishlist.go_to_catalog()
        catalogpage = CatalogPage(self.driver)
        catalogpage.add_product_to_wishlist()
        homepage_wishlist.go_to_wishlist()
        homepage_wishlist.delete_product()






