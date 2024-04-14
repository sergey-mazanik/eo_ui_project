from pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import create_account_locators


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create'
