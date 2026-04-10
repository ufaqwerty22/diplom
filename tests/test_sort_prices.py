from playwright.sync_api import expect

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage


def test_sort_prices(page):
    main_page = MainPage(page)
    catalog_page = CatalogPage(page)
    main_page.open()
    main_page.get_header_bottom_component().click_menu_item_by_text('Детская')
    catalog_page.get_sort_component().click_sort_by_text('возрастанию цены')

    for i in range(59):
        current_price = catalog_page.get_catalog_component().wrapper.locator(
            f'(//div[contains(@class, "current-price")])[{i + 1}]').inner_text()
        next_price = catalog_page.get_catalog_component().wrapper.locator(
            f'(//div[contains(@class, "current-price")])[{i + 2}]').inner_text()
        current_price_value = int(''.join(filter(str.isdigit, current_price)))
        next_price_value = int(''.join(filter(str.isdigit, next_price)))

        assert current_price_value <= next_price_value