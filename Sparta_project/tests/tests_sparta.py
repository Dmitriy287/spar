from Sparta_project.config.config_sparta import *
from Sparta_project.locators.locators_sparta import *
from Sparta_project.data.data_sparta import *
from playwright.sync_api import expect


@pytest.fixture
def start_page(page: Page):
    def start_page_func():
        page.goto(data_test)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/start_page.png")
    return start_page_func



@pytest.fixture
def menu(page: Page):
    def menu_func():
        page.goto(data_test)
        page.click(locator_clothe)
        page.click(locator_shapki)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/menu.png")
    return menu_func

@pytest.fixture
def menu1(page: Page):
    def menu1_func():
        page.goto(data_test)
        page.click(locator_clothe)
        page.click(locator_shapki)
        page.wait_for_timeout(2000)
        page.click(locator_shapka_tropdown)
        page.screenshot(path="screenshots/menu1.png")
    return menu1_func


@pytest.fixture
def katalog_tovarov(page: Page):
    def katalog_tovarov_func():
        page.goto(data_test)
        page.wait_for_selector(locator_kimono)
        element = page.locator(locator_kimono)
        if element.is_hidden():
            raise Exception("Element is hidden and cannot be clicked")
        page.click(locator_kimono)
        page.wait_for_timeout(1000)
        page.click(locator_kimono_karate)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/kimono.png")
        page.wait_for_timeout(2000)
    return katalog_tovarov_func

@pytest.fixture
def basket(page: Page):
    def basket_func():
        page.goto(data_test)
        page.click(locator_rashgardi)
        page.wait_for_timeout(2000)
        page.click(locator_sort)
        page.wait_for_timeout(1000)
        page.click(locator_date)
        page.wait_for_timeout(1000)
        page.click(locator_rashgardi_child)
        page.click(locator_in_basket)
        page.wait_for_timeout(1000)
        page.click(locator_basket)
        page.screenshot(path="screenshots/basket.png")
        page.wait_for_timeout(2000)
        page.click(locator_delete_basket)
        page.wait_for_timeout(1000)
    return basket_func



@pytest.fixture
def ataka(page: Page):
    def ataka_func():
        page.goto(data_test)
        page.fill(locator_button_catalog, data_catalog)
        assert page.title() == 'SPARTA - Спортивный магазин экипировки и одежды для единоборств в Новосибирске'
        page.wait_for_timeout(1000)
        page.click(locator_button_find)
        page.click(locator_button_basket)
        page.wait_for_timeout(3000)
        page.click(locator_buy)
        page.wait_for_timeout(3000)
        page.fill(locator_name, data_name)
        page.fill(locator_phone, data_phone)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/ataka.png")
        page.wait_for_timeout(2000)
    return ataka_func


@pytest.fixture
def sravni(page: Page):
    def sravni_func():
        page.goto(data_test)
        # Wait for the element to be visible before clicking
        page.wait_for_selector(locator_kimono)
        element = page.locator(locator_kimono)
        # Ensure the element is not hidde
        if element.is_hidden():
            raise Exception("Element is hidden and cannot be clicked")
        page.click(locator_kimono)
        page.wait_for_timeout(1000)
        page.click(locator_sort)
        page.wait_for_timeout(2000)
        page.click(locator_sort1)
        page.wait_for_timeout(2000)
        page.click(locator_srav_kim)
        page.wait_for_timeout(2000)
        page.click(locator_srav_kim1)
        page.wait_for_timeout(1000)
        page.click(locator_sravnenie)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/ataka1.png")
    return sravni_func