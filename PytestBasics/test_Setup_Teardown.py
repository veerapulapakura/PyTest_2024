from selenium import webdriver

driver=None
def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.facebook.com/")


def teardown_module():
    driver.quit()

def test_facebook():
    assert driver.title == 'Facebook – log in or sign up'


def test_facebook_currentUrl():
    assert driver.current_url=='https://www.facebook.com/'


