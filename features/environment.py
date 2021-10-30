from behave import *
from utils.browserActions import BrowserActions as act

def before_all(context):
    browser = act.getBrowser()
    context.browser = act(browser)
    context.testData = {}

def after_all(context):
    try: context.browser.quit()
    except: pass