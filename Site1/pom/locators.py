from selenium.webdriver.common.by import By


class HomePageLocators():
    SEARCH_ICON = (By.ID, 'header-search')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.digi-search-form__input-block>input')
    SEARCH_BTN = (By.CSS_SELECTOR, 'button.digi-search-form__submit')
