from playwright.sync_api import expect

from pages.main_page import MainPage


def test_search_not_exists_product(page):
    main_page = MainPage(page)
    main_page.open()
    main_page.get_header_bottom_component().click_search_button()
    main_page.get_header_bottom_component().fill_search_field('qwerty')
    main_page.get_header_bottom_component().click_enter_search_field()

    expect(main_page.get_search_empty_component().wrapper).to_contain_text(
        'По этому запросу ничего не находится')