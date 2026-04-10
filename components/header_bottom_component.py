from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.button_control import ButtonControl


class HeaderBottomComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
        self.__search_button = ButtonControl(self.page, self.wrapper.locator('a#headerSearchTrigger'))
        self.__search_input = ButtonControl(self.page, self.wrapper.locator('input.header-search__input'))

    def click_search_button(self):
        self.__search_button.click_anyway()

    def fill_search_field(self, text: str):
        self.__search_input.fill(text)

    def click_enter_search_field(self):
        self.__search_input.wrapper.press('Enter')

    def click_menu_item_by_text(self, text: str):
        self.wrapper.get_by_text(text, exact=True).click()

    def hover_over_text(self, text: str):
        self.wrapper.get_by_text(text, exact=True).hover()

    def click_drop_down_item_by_text(self, text: str):
        self.wrapper.get_by_text(text, exact=True).click()