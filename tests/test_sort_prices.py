import os

import allure
from playwright.sync_api import expect

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage


@allure.title('Работа сортировки по возрастающей цене')
def test_sort_prices(page):
    main_page = MainPage(page)
    catalog_page = CatalogPage(page)

    main_page.open()
    main_page.get_header_bottom_component().click_menu_item_by_text('Детская')
    catalog_page.get_sort_component().click_sort_by_text('возрастанию цены')
    count_prices = catalog_page.get_sort_component().compare_prices_from_lo_to_high()

    assert count_prices == 59