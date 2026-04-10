from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class CheckoutContainerComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_total_price(self):
        return self.wrapper.locator('div.basket-coupon-block-total-price-current')