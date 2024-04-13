from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.EcoFriendlyPage import EcoFriendlyPage
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver


@pytest.fixture()
def eco_page(driver):
    return EcoFriendlyPage(driver)
