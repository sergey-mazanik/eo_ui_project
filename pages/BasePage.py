from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import base_locators as base_loc


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.actions = ActionChains(self.driver)

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            self.driver.get(f'{self.base_url}')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def check_that_current_page_is_open(self, text):
        current_product_page_header_title = self.find(base_loc.page_header_title_locator).text
        assert text == current_product_page_header_title, 'Wrong page is open'

    def check_that_adv_is_on_page(self):
        self.wait.until(ec.presence_of_element_located(base_loc.iframe))
        self.driver.switch_to.frame(self.find(base_loc.iframe))
        self.wait.until(ec.visibility_of(self.find(base_loc.adv_locator)))
