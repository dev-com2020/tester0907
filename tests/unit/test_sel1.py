import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def test_basic_options_chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(3)
    driver.quit()

# def test_basic_options_firefox():
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     driver.get("https://www.google.com")
#     time.sleep(2)
#     driver.quit()

# def test_basic_options_ie():
#     driver = webdriver.Ie()
#     driver.get("https://www.google.com")
#     time.sleep(2)
#     driver.quit()

def test_basic_options_edge():
    driver = webdriver.Edge()
    driver.get("https://www.google.com")
    time.sleep(3)
    driver.quit()

# def test_basic_options_opera():
#     driver = webdriver.Opera()
#     driver.get("https://www.google.com")
#     time.sleep(2)
#     driver.quit()

# def test_basic_options_safari():
#     driver = webdriver.Safari()
#     driver.get("https://www.google.com")
#     time.sleep(2)
#     driver.quit()
#
