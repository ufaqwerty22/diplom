from playwright.sync_api import Page, Locator

from components.catalog_component import CatalogComponent
from components.filter_prices_component import FilterPricesComponent
from components.sort_component import SortComponent
from pages.base_page import BasePage


class CatalogPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, 'https://www.olant-shop.ru/catalog')

    def get_catalog_component(self):
        return CatalogComponent(self.page, self.page.locator('div.catalog-list.row'))

    def get_sort_component(self):
        return SortComponent(self.page, self.page.locator('div.catalog-sort__box'))

    def get_filter_prices_component(self):
        return FilterPricesComponent(self.page, self.page.locator('div.catalog-filter'))