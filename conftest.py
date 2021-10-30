import pytest
import pathlib
from selenium import webdriver
from pytest_cases import parametrize_with_cases, parametrize
from utils.config import Config

@pytest.fixture
def testData():
    return {}

@pytest.fixture
def browser(testData):
    remote = False
    config = Config().getConfig()
    remote = config.browser.isGrid
    exec_path = str(pathlib.Path().absolute().parent.joinpath(config.browser.default_browser_path))
    if remote:
        driver = webdriver.Remote(
                                  executable_path=exec_path,
                                  command_executor=config.gridHost,
                                  desired_capabilities=config.browser.default_browser_profile
                                 )
    else:
        driver = webdriver.Chrome(executable_path=exec_path, chrome_options={})
    driver.maximize_window()

    testData["session_id"] = driver.session_id
    yield driver
    driver.quit()


