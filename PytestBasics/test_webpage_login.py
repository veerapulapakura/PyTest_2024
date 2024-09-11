from selenium import webdriver

#driver = webdriver.Chrome(executable_path='/Users/veerapulapakura/Documents/Drivers/chromedriver.exe')
#driver = webdriver.Chrome(executable_path='/Users/veerapulapakura/Documents/Drivers/chromedriver.exe')

def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    assert driver.title == 'Google'
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    assert driver.title == 'Facebook – log in or sign up'
    driver.quit()

def test_gmail():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.gmail.com/")
    assert driver.title == 'Gmail'
    driver.quit()

