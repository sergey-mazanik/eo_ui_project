from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.EcoFriendlyPage import EcoFriendlyPage
from pages.SalePage import SalePage
from pages.CreateAccauntPage import CreateAccountPage
import pytest
import allure


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    allure.attach(chrome_driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    chrome_driver.quit()


@pytest.fixture()
def eco_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)
