import os

import allure
from playwright.sync_api import expect

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@allure.title('Страница товара')
def test_product_page(page):
    main_page = MainPage(page)
    catalog_page = CatalogPage(page)
    product_page = ProductPage(page, '16399284')

    main_page.open()
    main_page.get_header_bottom_component().click_menu_item_by_text('Коляски')

    expect(main_page.page).to_have_url(f'{os.getenv('MAIN_PAGE_URL')}catalog/kolyaski/')

    catalog_page.get_catalog_component().click_product_by_name('Elodie косметичка - Meadow Blossom')
    catalog_page.page.wait_for_timeout(1000)

    expect(product_page.get_name_product_component().wrapper).to_contain_text('Elodie косметичка - Meadow Blossom')
    expect(product_page.get_card_main_component().get_photo_locator()).to_be_visible()
    expect(product_page.get_card_aside_component().get_price_locator()).to_be_visible()

