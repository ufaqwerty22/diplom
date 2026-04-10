import os

from playwright.sync_api import Locator, expect

from pages.main_page import MainPage
from pages.catalog_page import CatalogPage


def test_drop_down(page):
    main_page = MainPage(page)
    catalog_page = CatalogPage(page)
    count_products = 0

    main_page.open()
    main_page.get_header_bottom_component().hover_over_text('Коляски')
    main_page.get_header_bottom_component().click_drop_down_item_by_text('Прогулочные коляски')

    expect(catalog_page.page).to_have_url(f'{os.getenv('MAIN_PAGE_URL')}catalog/progulochnye-kolyaski/')
    for number in range(60):
        title = catalog_page.get_catalog_component().wrapper.locator(
            f'(//div[contains(@class, "col-lg-3 col-md-4")])[{number + 1}]').inner_text()
        if 'коляска' in title.lower():
            count_products += 1

    assert count_products == 60