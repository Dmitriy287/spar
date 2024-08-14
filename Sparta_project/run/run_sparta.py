from Sparta_project.tests.tests_sparta import *


@pytest.mark.smoke
def test_start_page(page: Page, start_page):
    start_page()

@pytest.mark.smoke
def test_menu(page: Page, menu):
        menu()

@pytest.mark.smoke
def test_menu1(page: Page, menu1):
        menu1()

@pytest.mark.smoke
def test_katalog_tovarov(page: Page, katalog_tovarov):
        katalog_tovarov()

@pytest.mark.smoke
def test_basket(page: Page, basket):
    basket()

@pytest.mark.smoke
def test_ataka(page: Page, ataka):
    ataka()

@pytest.mark.smokegit
def test_sravni(page: Page, sravni):
    sravni()

