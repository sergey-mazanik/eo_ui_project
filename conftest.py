from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.EcoFriendlyPage import EcoFriendlyPage
from pages.SalePage import SalePage
from pages.CreateAccauntPage import CreateAccountPage
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


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)
