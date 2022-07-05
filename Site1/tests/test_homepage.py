import time

import pytest
from auto_site.autotest_practice_1.Site1.pom.homepage_nav import HomepageNav
from auto_site.autotest_practice_1.Site1.pom.homepage_search import HomepageSearch


@pytest.mark.usefixtures('setup')
class TestHomepage:

    # Проверяем наличие (соответствие с NAV_LINK_TEXT) категорий навигационной панели
    # def test_nav_links(self):
    #     homepage_nav = HomepageNav(self.driver)
    #     actual_links = homepage_nav.get_nav_links_text()
    #     expected_links = homepage_nav.NAV_LINK_TEXT
    #     assert expected_links == actual_links, 'Validating Nav Link Text'
    #     # Проходим по всем категориям
    #     for index in range(4):
    #         homepage_nav.get_nav_links()[index].click()
    #         time.sleep(3)

    # Проверяем работу поисковой строки
    def test_search(self):
        homepage_search = HomepageSearch(self.driver)
        assert homepage_search.should_be_search_icon(), 'Search icon not found'
        assert homepage_search.go_to_search(), 'Search button not found'
        assert homepage_search.send_keys_to_search(), 'Search error'


