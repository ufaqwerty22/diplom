from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class BreadcrumbsComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def click_breadcrumbs_by_text(self, text: str):
        self.wrapper.get_by_text(text).click()