from playwright.sync_api import expect

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage


def test_filter_prices(page):
    main_page = MainPage(page)
    catalog_page = CatalogPage(page)
    main_page.open()
    main_page.get_header_bottom_component().click_menu_item_by_text('Кормление')
    main_page.page.mouse.move(0,30)
    catalog_page.get_filter_prices_component().hover_and_click_by_text('Цена')
    catalog_page.get_filter_prices_component().enter_min_price('500')
    catalog_page.get_filter_prices_component().enter_max_price('2500')
    catalog_page.get_filter_prices_component().click_submit_button()
    for i in range(60):
        price = catalog_page.get_catalog_component().wrapper.locator(
            f'(//div[contains(@class, "current-price")])[{i + 1}]').inner_text()
        price_value = int(''.join(filter(str.isdigit, price)))

        assert 500 <= price_value <= 2500