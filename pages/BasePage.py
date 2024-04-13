from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


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
