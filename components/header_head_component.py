from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.button_control import ButtonControl


class HeaderHeadComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_button_by_text(self, text: str):
        return ButtonControl(self.page, self.wrapper.get_by_text(text))

    def click_button_by_text(self, text: str):
        self.get_button_by_text(text).click_anyway()