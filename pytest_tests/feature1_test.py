import pytest

from utils.browserActions import BrowserActions as act
from utils.locators import MainPageLocators, nPageLocators, Urls
def test_withPyTest(browser, testData):
     actions = act(browser) #browser type/distribution from the config/runtime
     print(f"\nsession_id: {testData['session_id']} saved in Test Data")
     actions.navigateToUrl(Urls.MAIN_URL, timeout=3)
     elem = actions.isElementExist(MainPageLocators.SEARCH_INPUT, 0)
     actions.highlight(elem, 3)
     print(f"session_id: {browser.session_id} passed")



