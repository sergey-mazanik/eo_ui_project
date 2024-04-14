def test_header_title_is_correct(create_account_page):
    create_account_page.open_page()
    create_account_page.check_that_current_page_is_open('Create New Customer Account')
