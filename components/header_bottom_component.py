import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.button_control import ButtonControl


class HeaderBottomComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
        self.__search_button = ButtonControl(self.page, self.wrapper.locator('a#headerSearchTrigger'))
        self.__search_input = ButtonControl(self.page, self.wrapper.locator('input.header-search__input'))

    def click_search_button(self):
        with allure.step('Нажать на кнопку поиска'):
            self.__search_button.click_anyway()

    def fill_search_field(self, text: str):
        with allure.step(f'Ввести {text} в поле поиска'):
            self.__search_input.fill(text)

    def click_enter_search_field(self):
        with allure.step('Нажать на Enter в поле поиска'):
            self.__search_input.wrapper.press('Enter')

    def click_menu_item_by_text(self, text: str):
        with allure.step(f'Нажать на пункт меню {text}'):
            self.wrapper.get_by_text(text, exact=True).click()

    def hover_over_text(self, text: str):
        with allure.step(f'Навести курсор на {text}'):
            self.wrapper.get_by_text(text, exact=True).hover()

    def click_drop_down_item_by_text(self, text: str):
        with allure.step(f'Нажать на пункт выпадающего меню {text}'):
            self.wrapper.get_by_text(text, exact=True).click()