from selenium import webdriver
import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture()
def crome_browser(request):
    driver=webdriver.Remote("http:\\35.226.56.28:4444\wd\hub", desired_capabilities= {'browserName': 'chrome', 'platform': 'ANY', 'version': ''})
    # driver = webdriver.Remote(
    #     command_executor='http://35.226.56.28:4444/wd/hub',
    #     desired_capabilities=DesiredCapabilities.CHROME)
    # request.
    return driver

def test_grid(crome_browser):
    crome_browser.get("http://google.com")
    if not "Google" in crome_browser.title:
        print ("ytn")
