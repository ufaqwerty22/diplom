from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from components.search_result_component import SearchResultComponent


class SearchResultFieldComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_search_result_component(self):
        return SearchResultComponent(self.page, self.wrapper.locator('//div[@class="digi-products-grid"]'))
