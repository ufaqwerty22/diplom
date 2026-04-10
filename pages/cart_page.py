from playwright.sync_api import Page, Locator

from components.checkout_container_component import CheckoutContainerComponent
from components.list_of_products_component import ListOfProductsComponent
from components.product_in_cart_component import ProductInCartComponent
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, 'https://www.olant-shop.ru/personal/cart/')

    def get_list_of_products_component(self):
        return ListOfProductsComponent(self.page, self.page.locator('div.basket-items-list-wrapper'))

    def get_component_product_in_cart_by_name(self, name: str):
        return ProductInCartComponent(self.page, self.page.locator(f'//span[contains(text(), "{name}")]/ancestor::tr'))

    def get_checkout_container_component(self):
        return CheckoutContainerComponent(self.page, self.page.locator('div.basket-checkout-container'))