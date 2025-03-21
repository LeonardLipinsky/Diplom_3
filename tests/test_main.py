from pages.main_page import MainPage
from pages.feed_page import FeedPage
from conftest import *
import allure


class TestMain:

    @allure.title('Проверка перехода по клику на Конструктор')
    def test_navigate_to_constructor_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_header_feed_button()
        main_page.click_constructor_button()
        assert 'Соберите бургер' in main_page.get_text_header_constructor()

    @allure.title('Проверка перехода по клику на Ленту заказов')
    def test_navigate_to_order_history_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        assert feed_page.get_text_title_order_list() == 'Лента заказов'

    @allure.title('Проверка отображения окна Детали ингредиента при клике на ингредиент')
    def test_displaying_modal_window_details_of_ingredient_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.check_detail_modal_display()

    @allure.title('Проверка закрытия окна Детали ингредиента кликом по крестику')
    def test_close_modal_window_details_of_ingredient_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.check_detail_modal_not_display()

    @allure.title('Проверка увеличения числа на счетчике при добавлении ингредиента в заказ')
    def test_changing_counter_for_ingredients_in_order_success(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_order_ingredient()
        assert main_page.get_count_ingredients() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_making_order_by_authenticated_user_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        main_page.click_login_button_main()
        main_page.drag_and_drop_order_ingredient()
        main_page.click_button_create_order()
        assert main_page.check_display_confirmation_modal()