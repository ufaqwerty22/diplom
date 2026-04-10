from playwright.sync_api import Page, Locator

from components.breadcrumbs_component import BreadcrumbsComponent
from components.card_aside_column_component import CardAsideColumnComponent
from components.card_main_column_component import CardMainColumnComponent
from components.name_product_component import NameProductComponent
from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page, id: str):
        super().__init__(page, f'https://www.olant-shop.ru/product/{id}')

    def get_breadcrumbs_component(self):
        return BreadcrumbsComponent(self.page, self.page.locator('div.breadcrumbs'))

    def get_name_product_component(self):
        return NameProductComponent(self.page, self.page.locator('h1.hidden-xs'))

    def get_card_main_component(self):
        return CardMainColumnComponent(self.page, self.page.locator('div.card-main-column'))

    def get_card_aside_component(self):
        return CardAsideColumnComponent(self.page, self.page.locator('div.card-aside-column'))

