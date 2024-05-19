from faker import Faker
import pytest


@pytest.mark.smoke
def test_header_title_is_correct(create_account_page):
    create_account_page.open_page()
    create_account_page.check_that_current_page_is_open('Create New Customer Account')


@pytest.mark.skip
def test_adv_is_on_page(create_account_page):
    create_account_page.open_page()
    create_account_page.check_that_adv_is_on_page()


@pytest.mark.smoke
def test_correct_create_account(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_creating_form('test', 'test', Faker().email(), 'testTEST123')
    create_account_page.check_that_account_page_is_open()
    create_account_page.check_that_congrats_notice_is_present()


@pytest.mark.regression
def test_create_account_without_password(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_creating_form('test', 'test', Faker().email(), '')
    create_account_page.check_that_error_is_present()
