#import pytest
import sys, pathlib
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.keys import Keys
import time, logging
from contextlib import contextmanager
from utils.config import Config

logging.basicConfig(filename="log.txt", level=logging.INFO)

class BrowserActions():
    _driver = None

    def wait_for_new_page_load(self, timeout=10): #todo hash changes
        old_page = self._driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(self._driver, timeout).until(staleness_of(old_page))

    @contextmanager
    def is_page_loaded(self, timeout=5):
        ok = WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )
        yield

        if not self._driver.execute_script("return document.readyState;") == "complete":
            raise Exception(f"Can't load page within {timeout}s")
        return ok

    @contextmanager
    def is_element_found(self, element_locator, timeout=0):
        if isinstance(element_locator, selenium.webdriver.remote.webelement.WebElement):
            raise Exception(f"Element locator is incorrect {element_locator}")
        try:
            element_found = WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located(element_locator))
            yield
        except:
            raise Exception(f"Element locator {element_locator} is NOT found")

        return element_found

    def isElementExist(self, element_locator, timeout=0):
        elem = None
        try:
            elem = WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located(element_locator))
            return elem
        except Exception as exc:
            self._driver.quit()
            print(f"Browser closed, error in {__file__} line: {sys.exc_info()[-1].tb_lineno}")
            raise Exception(f"Element locator {element_locator} is NOT found")

    def __init__(self, driver=None):
        self._driver = driver

    @staticmethod
    def getBrowser(): #todo factory by browser type/options
        config = Config().getConfig()
        exec_path = str(pathlib.Path().absolute().parent.joinpath(config.browser.default_browser_path))
        driver = webdriver.Chrome(executable_path=exec_path, chrome_options={})
        driver.maximize_window()
        return driver

    def highlight(self, element, effect_time=5, color='red', border=5):
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = element.get_attribute('style')
        apply_style("border: {0}px solid {1};".format(border, color))
        time.sleep(effect_time)
        apply_style(original_style)
        # This will add red 5 pixels border to element for 5 seconds

    def navigateToUrl(self, url, timeout=5):
        print(f"\nGoTo url: {url}")
        with self.is_page_loaded(timeout=timeout):
            self._driver.get(url)

    def sendKeys(self, element_locator, keys, timeout=0):
        if isinstance(element_locator, selenium.webdriver.remote.webelement.WebElement):
            element_locator.send_keys(*keys)
            return
        if timeout > 0:
            with self.is_element_found(element_locator, timeout) as element:
                element.send_keys(*keys)
        else:
            self._driver.find_element(*element_locator).send_keys(*keys)

    def getAttrValue(self, element_locator, attr='text', timeout=0):
        return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(element_locator)).get_attribute(attr)

    def click(self, element_locator, timeout=0):
        return WebDriverWait(self._driver, timeout).until(EC.element_to_be_clickable(element_locator)).click()

