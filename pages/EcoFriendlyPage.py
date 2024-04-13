from pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec

products_list_locator = ('class name', 'product-item-info')
add_to_compare_button_locator = ('xpath', '//*[@title="Add to Compare"]')
compare_section_locator = ('class name', 'odd')
add_to_cart_button_locator = ('xpath', '(//*[@title="Add to Cart"])[1]')
notification_alert_locator = ('xpath', '//*[@data-ui-id="message-notice"]/div')
page_header_title_locator = ('xpath', '//*[@data-ui-id="page-title-wrapper"]')


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'
    product_name = None

    def move_to_product(self):
        products_list = self.find_all(products_list_locator)
        self.product_name = products_list[0].text.split('\n')[0]
        self.actions.move_to_element(products_list[0])

    def add_product_to_compare(self):
        add_to_compare_button = self.find(add_to_compare_button_locator)
        self.actions.click(add_to_compare_button)
        self.actions.perform()

    def add_product_to_cart(self):
        add_to_cart_button = self.find(add_to_cart_button_locator)
        self.actions.click(add_to_cart_button)
        self.actions.perform()

    def check_that_product_added_to_compare(self):
        self.wait.until(ec.presence_of_element_located(compare_section_locator))
        compare_product = self.find(compare_section_locator).text.split('\n')[0]
        assert self.product_name == compare_product, 'Wrong product added to compare'

    def check_that_page_has_alert(self, text):
        self.wait.until(ec.presence_of_element_located(notification_alert_locator))
        alert_text = self.find(notification_alert_locator).text
        assert alert_text == text, 'Wrong alert text'

    def check_that_current_page_is_open(self, text):
        current_product_page_header_title = self.find(page_header_title_locator).text
        assert text == current_product_page_header_title, 'Wrong product page is open'

    def check_that_right_product_page_is_open(self):
        current_product_page_header_title = self.find(page_header_title_locator).text
        assert self.product_name == current_product_page_header_title, 'Wrong product page is open'
