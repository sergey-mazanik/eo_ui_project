from pages.BasePage import BasePage
from pages.locators import create_account_locators as ca_loc


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create'

    def fill_creating_form(self, first_name, last_name, email, password):
        self.find(ca_loc.first_name_field_locator).send_keys(first_name)
        self.find(ca_loc.last_name_field_locator).send_keys(last_name)
        self.find(ca_loc.email_field_locator).send_keys(email)
        self.find(ca_loc.password_field_locator).send_keys(password)
        self.find(ca_loc.confirm_password_field_locator).send_keys(password)
        self.find(ca_loc.submit_button_locator).click()

    def check_that_account_page_is_open(self):
        header = self.find(ca_loc.account_header_title_locator).text
        assert header == 'My Account'

    def check_that_congrats_notice_is_present(self):
        congrats_notice = self.find(ca_loc.congrats_notice_locator).text
        assert congrats_notice == 'Thank you for registering with Main Website Store.'

    def check_that_error_is_present(self):
        password_error = self.find(ca_loc.password_error_locator).text
        confirm_password_error = self.find(ca_loc.confirm_password_error_locator).text
        assert password_error == 'This is a required field.'
        assert confirm_password_error == 'This is a required field.'
