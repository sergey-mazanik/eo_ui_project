from pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import eco_locators as eco_loc
from pages.locators import base_locators as base_loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'
    product_name = None

    def move_to_product(self):
        products_list = self.find_all(eco_loc.products_list_locator)
        self.product_name = products_list[0].text.split('\n')[0]
        self.actions.move_to_element(products_list[0])

    def add_product_to_compare(self):
        add_to_compare_button = self.find(eco_loc.add_to_compare_button_locator)
        self.actions.click(add_to_compare_button)
        self.actions.perform()

    def add_product_to_cart(self):
        add_to_cart_button = self.find(eco_loc.add_to_cart_button_locator)
        self.actions.click(add_to_cart_button)
        self.actions.perform()

    def check_that_product_added_to_compare(self):
        self.wait.until(ec.presence_of_element_located(eco_loc.compare_section_locator))
        compare_product = self.find(eco_loc.compare_section_locator).text.split('\n')[0]
        assert self.product_name == compare_product, 'Wrong product added to compare'

    def check_that_page_has_alert(self, text):
        self.wait.until(ec.presence_of_element_located(eco_loc.notification_alert_locator))
        alert_text = self.find(eco_loc.notification_alert_locator).text
        assert alert_text == text, 'Wrong alert text'

    def check_that_right_product_page_is_open(self):
        current_product_page_header_title = self.find(base_loc.page_header_title_locator).text
        assert self.product_name == current_product_page_header_title, 'Wrong product page is open'

    def choose_product_size(self):
        self.find(eco_loc.product_size_locator).click()

    def choose_product_color(self):
        self.find(eco_loc.product_color_locator).click()

    def check_that_product_added_to_cart(self):
        self.wait.until(ec.text_to_be_present_in_element(eco_loc.counter_number_locator, '1'))
        assert self.find(eco_loc.counter_number_locator).text == '1', 'Product is not added to cart'
