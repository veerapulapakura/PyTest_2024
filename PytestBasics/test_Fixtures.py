import pytest
from selenium import webdriver

driver=None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print('-----   Setup method   ------')
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.facebook.com/")

    yield
    print(' -----   Setup method   ------ ')
    driver.quit()

def test_facebook(init_driver):
    assert driver.title == 'Facebook – log in or sign up'

def test_facebook_currentUrl(init_driver):
    assert driver.current_url=='https://www.facebook.com/'

