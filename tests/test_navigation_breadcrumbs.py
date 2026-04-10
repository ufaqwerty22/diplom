import os

from playwright.sync_api import expect

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_navigation_breadcrumbs(page):
    main_page = MainPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page, '16872398')
    main_page.open()
    main_page.get_header_bottom_component().click_menu_item_by_text('Мамам')
    catalog_page.get_catalog_component().click_product_by_name('Elodie сумка Changing Bag Garden Leo Toile')
    product_page.get_breadcrumbs_component().click_breadcrumbs_by_text('Интернет магазин детских товаров')

    expect(main_page.page).to_have_url(f'{os.getenv('MAIN_PAGE_URL')}')