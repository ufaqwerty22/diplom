import os

from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage


def test_cart(page):
    main_page = MainPage(page)
    catalog_page = CatalogPage(page)
    cart_page = CartPage(page)
    main_page.open()
    main_page.get_header_bottom_component().click_menu_item_by_text('Детская')
    catalog_page.get_catalog_component().add_product_in_cart_by_name(
        f'{os.getenv('NAME_OF_PRODUCT')}')
    catalog_page.page.wait_for_timeout(1500)
    catalog_page.get_added_to_cart_component().click_go_to_cart()
    cart_page.get_component_product_in_cart_by_name(f'{os.getenv('NAME_OF_PRODUCT')}').click_delete_product_btn()
    cart_page.page.wait_for_timeout(500)

    expect(cart_page.get_checkout_container_component().get_total_price()).to_contain_text("0 руб.")
