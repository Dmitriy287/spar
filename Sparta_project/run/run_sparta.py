from Sparta_project.tests.tests_sparta import *
from Sparta_project.config.config_sparta import *


@pytest.mark.smoke
def test_start_page(page: Page, start_page):
    start_page()


@pytest.mark.smoke
def test_menu(page: Page, menu):
    menu()


@pytest.mark.smoke
def test_product_catalog(page: Page, product_catalog):
    product_catalog()


@pytest.mark.smoke
def test_basket(page: Page, basket):
    basket()


@pytest.mark.smoke
def test_one_click(page: Page, one_click):
    one_click()


@pytest.mark.smoke
def test_comparison(page: Page, comparison):
    comparison()


@pytest.mark.smoke
def test_selection_by_parameters(page: Page, selection_by_parameters):
    selection_by_parameters()


@pytest.mark.smoke
def test_favourites(page: Page, favourites):
    favourites()


