from playwright.sync_api import Page, Locator

from components.header_bottom_component import HeaderBottomComponent
from components.header_head_component import HeaderHeadComponent
from components.header_top_component import HeaderTopComponent
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, 'https://www.olant-shop.ru/')