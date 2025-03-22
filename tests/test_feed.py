from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.account_page import AccountPage
from conftest import *
import allure


class TestFeed:

    @allure.title('Проверка открытия всплывающего окна с деталями при клике на заказ')
    def test_displaying_modal_order_details_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        feed_page.click_order()
        assert 'бургер' in feed_page.get_text_header_modal_order()

    @allure.title('Проверка отображения существующего заказа из истории пользователя в ленте')
    def test_displaying_in_feed_new_order_from_history_success(self, driver, create_user_and_order_and_delete,
                                                               set_user_tokens):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_personal_account_header()
        account_page.click_order_history_button()
        order_id = order_history_page.get_id_order_card()
        main_page.click_header_feed_button()
        assert feed_page.check_id_order_feed(order_id)

    @allure.title('Проверка увеличения числа на счетчике общего количества выполненных заказов')
    def test_changes_counter_for_quantity_of_orders_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_quantity_orders()
        main_page.click_constructor_button()
        main_page.click_login_button_main()
        main_page.drag_and_drop_order_ingredient()
        main_page.click_button_create_order()
        main_page.click_close_modal_button()
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_quantity_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка увеличения числа на счетчике ежедневного количества выполненных заказов')
    def test_changes_counter_for_daily_quantity_of_orders_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_daily_quantity_order()
        main_page.click_constructor_button()
        main_page.click_login_button_main()
        main_page.drag_and_drop_order_ingredient()
        main_page.click_button_create_order()
        main_page.click_close_modal_button()
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_daily_quantity_order()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка появления нового заказа в разделе В работе')
    def test_displaying_new_order_in_progress_feed_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_login_button_main()
        main_page.drag_and_drop_order_ingredient()
        main_page.click_button_create_order()
        new_order_id = main_page.get_order_number_modal()
        main_page.click_close_modal_button()
        main_page.click_header_feed_button()
        assert feed_page.get_order_id_feed_progress() == '0'+new_order_id