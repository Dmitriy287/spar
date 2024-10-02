from Sparta_project.config.config_sparta import *
from Sparta_project.locators.locators_sparta import *
from Sparta_project.data.data_sparta import *



@pytest.fixture
def start_page(page: Page):
    def start_page_func():
        page.goto(data_test)
        page.wait_for_timeout(2000)
        assert "https://sparta-outfit.ru/" in page.url.lower()
        page.screenshot(path="screenshots/start_page.png")
    return start_page_func


@pytest.fixture
def menu(page: Page):
    def menu_func():
        page.goto(data_test)
        page.click(locator_clothe1)
        page.wait_for_timeout(1000)
        page.click(locator_hats1)
        page.wait_for_timeout(2000)
        page.click(locator_a_cap)
        page.screenshot(path="screenshots/menu.png")
        assert "https://sparta-outfit.ru/" in page.url.lower()
        page.click(locator_logo)
        page.wait_for_timeout(1000)
    return menu_func


@pytest.fixture
def product_catalog(page: Page):
    def product_catalog_func():
        page.goto(data_test)
        page.click(locator_kimono1)
        page.wait_for_timeout(1000)
        page.click(locator_kimono_karate)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/product_catalog.png")
        assert page.inner_text('h1') == 'Кимоно для карате'
        page.click(locator_logo)
    return product_catalog_func


@pytest.fixture
def basket(page: Page):
    def basket_func():
        page.goto(data_test)
        page.click(locator_rash1)
        page.wait_for_timeout(2000)
        page.click(locator_sort)
        page.wait_for_timeout(1000)
        page.click(locator_date)
        page.wait_for_timeout(1000)
        page.click(locator_rash_child)
        page.click(locator_in_basket)
        page.wait_for_timeout(1000)
        page.click(locator_basket)
        page.screenshot(path="screenshots/basket.png")
        page.wait_for_timeout(2000)
        page.click(locator_delete_basket)
        assert page.title() == 'Корзина'
        page.wait_for_timeout(1000)
        page.click(locator_logo)
    return basket_func


@pytest.fixture
def one_click(page: Page):
    def one_click_func():
        page.goto(data_test)
        page.fill(locator_button_catalog, data_catalog)
        page.wait_for_timeout(1000)
        page.click(locator_button_find)
        page.click(locator_button_basket)
        page.wait_for_timeout(3000)
        page.click(locator_buy)
        page.wait_for_timeout(2000)
        page.click(locator_plus)
        page.click(locator_cupon)
        page.fill(locator_field_cupon, data_cupon)
        page.wait_for_timeout(2000)
        page.fill(locator_firstname, data_firstname)
        page.fill(locator_lastname, data_lastname)
        page.fill(locator_phone, data_phone)
        page.fill(locator_email, data_email)
        page.wait_for_timeout(2000)
        assert page.is_visible(locator_basket)
        page.screenshot(path="screenshots/one_click.png")
        page.wait_for_timeout(2000)
    return one_click_func


@pytest.fixture
def comparison(page: Page):
    def comparison_func():
        page.goto(data_test)
        page.click(locator_kimono1)
        page.wait_for_timeout(1000)
        page.click(locator_sort)
        page.wait_for_timeout(2000)
        page.click(locator_sort1)
        page.wait_for_timeout(2000)
        page.click(locator_comparison_kim)
        page.wait_for_timeout(2000)
        page.click(locator_comparison_kim1)
        page.wait_for_timeout(1000)
        page.click(locator_comparison)
        assert page.inner_text('h1') == 'Сравнить товары'
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/comparison.png")
        page.click(locator_logo)
    return comparison_func


@pytest.fixture
def selection_by_parameters(page: Page):
    def selection_by_parameters_func():
        page.goto(data_test)
        page.click(locator_clothe_season1)
        page.click(locator_t_shirts)
        page.wait_for_timeout(1000)
        page.fill(locator_field_1, data_field_1)
        page.fill(locator_field_2, data_field_2)
        page.wait_for_timeout(1000)
        page.click(locator_Manto)
        page.wait_for_timeout(1000)
        page.click(locator_size_s)
        page.wait_for_timeout(1000)
        page.click(locator_show)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/selection_by_parameters.png")
        page.click(locator_reset)
        assert "https://sparta-outfit.ru/" in page.url.lower()
        page.click(locator_logo)
        page.wait_for_timeout(2000)
    return selection_by_parameters_func


@pytest.fixture
def favourites(page: Page):
    def favourites_func():
        page.goto(data_test)
        page.fill(locator_button_catalog, data_catalog)
        page.wait_for_timeout(1000)
        page.click(locator_button_find)
        page.click(locator_plus_favourites)
        page.wait_for_timeout(1000)
        page.click(locator_favourites)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/favourites.png")
        page.click(locator_clear_favourites)
        assert page.is_visible(locator_favourites)
        page.click(locator_logo)
        page.wait_for_timeout(2000)
    return favourites_func