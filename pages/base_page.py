import allure
from playwright.sync_api import Page

from components.added_to_cart_component import AddedToCartComponent
from components.header_top_component import HeaderTopComponent
from components.header_head_component import HeaderHeadComponent
from components.header_bottom_component import HeaderBottomComponent
from components.search_empty_component import SearchEmptyComponent
from components.search_result_field_component import SearchResultComponent


class BasePage:
    def __init__(self, page: Page, url: str):
        self.page: Page = page
        self.url: str = url

    def open(self):
        with allure.step('Открыть страницу'):
            self.page.goto(self.url, timeout=1000000)

    def move_mouse(self, x: int, y: int):
        self.page.mouse.move(x, y)

    def get_header_head_component(self):
        return HeaderHeadComponent(self.page, self.page.locator('div.header-head'))

    def get_header_top_component(self):
        return HeaderTopComponent(self.page, self.page.locator('div.header-top'))

    def get_header_bottom_component(self):
        return HeaderBottomComponent(self.page, self.page.locator('div.header-bottom'))

    def get_search_result_component(self):
        return SearchResultComponent(self.page, self.page.locator('(//div[contains(@class, "digi-wrapper")])[2]'))

    def get_added_to_cart_component(self):
        return AddedToCartComponent(self.page, self.page.locator('div#addedToCartModal'))

    def get_search_empty_component(self):
        return SearchEmptyComponent(self.page, self.page.locator('div.digi-empty'))