import os

import allure
from playwright.sync_api import Locator, expect

from pages.main_page import MainPage
from pages.catalog_page import CatalogPage


@allure.title('Работа категорий меню')
def test_drop_down(page):
    main_page = MainPage(page)
    catalog_page = CatalogPage(page)

    main_page.open()
    main_page.get_header_bottom_component().hover_over_text('Коляски')
    main_page.get_header_bottom_component().click_drop_down_item_by_text('Прогулочные коляски')

    expect(catalog_page.page).to_have_url(f'{os.getenv('MAIN_PAGE_URL')}catalog/progulochnye-kolyaski/')
    count_products = catalog_page.get_catalog_component().count_products_by_word('коляска')
    assert count_products == os.getenv('MAX_COUNT_PRODUCTS')
