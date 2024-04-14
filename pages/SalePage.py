from pages.BasePage import BasePage
from pages.locators import sale_locators as sale_loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_that_promo_button_is_clickable(self):
        promo_button = self.find(sale_loc.shop_deals_button_locator)
        assert promo_button.is_enabled()

    def click_promo_button(self):
        self.find(sale_loc.shop_deals_button_locator).click()

    def check_that_new_page_is_open(self):
        assert f'{self.base_url}{self.page_url}' != self.driver.current_url

    def click_on_minicart_logo(self):
        self.find(sale_loc.minicart_logo_locator).click()

    def check_that_minicart_is_empty(self):
        minicart_text = self.find(sale_loc.minicart_content_locator).text
        assert minicart_text == 'You have no items in your shopping cart.', \
            'The minicart is not empty'
