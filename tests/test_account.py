from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from conftest import *
import allure


class TestAccount:

    @allure.title('Проверка перехода в профиль по клику на Личный кабинет в хэдере')
    def test_navigate_to_account_page_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        main_page.click_personal_account_header()
        account_page.wait_description_visibility()
        assert account_page.check_display_description() is True

    @allure.title('Проверка перехода по клику на История заказов')
    def test_navigate_to_order_history_page_success(self, driver, set_user_tokens, create_user_and_order_and_delete):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        main_page.click_personal_account_header()
        account_page.wait_description_visibility()
        account_page.click_order_history_button()
        order_history_page.wait_order_visibility()
        assert 'бургер' in order_history_page.get_text_order_card_header()

    @allure.title('Проверка выполнения логаута по кнопке Выйти')
    def test_logout_from_profile_page_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        main_page.click_personal_account_header()
        account_page.wait_description_visibility()
        account_page.click_exit_button()
        account_page.wait_register_button_visibility()
        assert account_page.check_display_register_button()