from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.button_control import ButtonControl


class HeaderTopComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
        self.__logo_button = ButtonControl(self.page, self.wrapper.locator('div.header-logo'))
        self.__number_button = ButtonControl(self.page, self.wrapper.locator('div.header-phones__number'))
        self.__wishlist_button = ButtonControl(self.page, self.wrapper.locator('a#wishlistFormTrigger'))
        self.__auth_button = ButtonControl(self.page, self.wrapper.locator('a#loginFormTrigger'))
        self.__cart_button = ButtonControl(self.page, self.wrapper.locator('a#headerCartTrigger'))

    def click_logo_button(self):
        self.__logo_button.click_anyway()

    def click_number_button(self):
        self.__number_button.click_anyway()

    def click_wishlist_button(self):
        self.__wishlist_button.click_anyway()

    def click_auth_button(self):
        self.__auth_button.click_anyway()

    def click_cart_button(self):
        self.__cart_button.click_anyway()