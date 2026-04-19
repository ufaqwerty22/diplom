import os

import allure
from playwright.sync_api import Locator, expect

from pages.main_page import MainPage
from pages.catalog_page import CatalogPage


@allure.title('Открытие главной страницы')
def test_main_page(page):
    main_page = MainPage(page)

    main_page.open()

    expect(main_page.page).to_have_url(os.getenv('MAIN_PAGE_URL'))