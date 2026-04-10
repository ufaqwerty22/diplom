from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class SearchResultComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_count_of_products(self):
        return self.wrapper.locator('//div[@class="digi-products-grid"]/div').count()

    def get_text_first_search_product(self):
        return (self.wrapper.locator
                ('(//div[contains(@class, "digi-product digi-product_ac")]//div[@class="digi-product__label"]/a)[1]'))