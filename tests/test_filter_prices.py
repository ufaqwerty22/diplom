import os

import allure
from playwright.sync_api import expect

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage


@allure.title('Работа фильтра по цене')
def test_filter_prices(page):
    main_page = MainPage(page)
    catalog_page = CatalogPage(page)

    main_page.open()
    main_page.get_header_bottom_component().click_menu_item_by_text('Кормление')
    main_page.move_mouse(0, 30)
    catalog_page.get_filter_prices_component().hover_and_click_by_text('Цена')
    catalog_page.get_filter_prices_component().enter_min_price('500')
    catalog_page.get_filter_prices_component().enter_max_price('2500')
    catalog_page.get_filter_prices_component().click_submit_button()
    count_prices = catalog_page.get_filter_prices_component().compare_prices_of_products(500, 2500)

    assert count_prices == 60