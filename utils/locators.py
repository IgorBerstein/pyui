from selenium.webdriver.common.by import By

class MainPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='id-search-field'][type='search']")

class nPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "#id-search-field")

class Urls:
    MAIN_URL = "http://www.python.org"