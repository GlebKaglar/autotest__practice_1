from selenium.webdriver.common.by import By


class HomePageLocators:

    """SEARCH ELEMENTS"""
    SEARCH_ELEMENT = (By.ID, 'header-search')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.digi-search-form__input-block>input')
    SEARCH_BTN = (By.CSS_SELECTOR, 'button.digi-search-form__submit')
    SEARCH_CLOSE_BTN = (By.CSS_SELECTOR, 'button.digi-search-form__close')

    """WISHLIST ELEMENTS"""
    WISHLIST_ELEMENT = (By.CLASS_NAME, 'th__wishlist')
    WISHLIST_GO_TO_CAT = (By.CSS_SELECTOR, 'a.btn-primary')
    WISHLIST_CLOSE = (By.CLASS_NAME, 'th__wishlist__modal__close')
    WISHLIST_UNHEART = (By.CLASS_NAME, 'th__wlmi__buttons__remove')
    WISHLIST_DELETE = (By.CLASS_NAME, 'th__cmi__buttons__red')
