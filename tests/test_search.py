import os

from playwright.sync_api import expect

from pages.main_page import MainPage


def test_search(page):
    main_page = MainPage(page)
    main_page.open()
    main_page.get_header_bottom_component().click_search_button()
    main_page.get_header_bottom_component().fill_search_field(f'{os.getenv('SEARCH_PRODUCT')}')

    assert main_page.get_search_result_component().get_count_of_products() > 0
    expect(main_page.get_search_result_component().get_text_first_search_product()).to_contain_text('бутылочка')
    expect(main_page.get_search_result_component().get_text_first_search_product()).to_contain_text('Tommee Tippee')