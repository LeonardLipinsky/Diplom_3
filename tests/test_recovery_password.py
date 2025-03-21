from pages.recovery_password_page import RecoveryPasswordPage
from pages.main_page import MainPage
from conftest import *
import allure


class TestRecoveryPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_navigate_to_recovery_passwd_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button_main()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_recovery_password_page()
        assert recovery_page.check_display_email_input()

    @allure.title('Проверка перехода к восстановлению пароля при вводе email')
    def test_click_recovery_button_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button_main()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_recovery_password_page()
        recovery_page.send_keys_email()
        recovery_page.click_recovery_password_button()
        assert recovery_page.check_display_password_input()

    @allure.title('Проверка отображения пароля в поле ввода после клика на иконку с глазом')
    def test_click_on_eye_icon_makes_passwd_visible_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button_main()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_recovery_password_page()
        recovery_page.send_keys_email()
        recovery_page.click_recovery_password_button()
        recovery_page.send_keys_password()
        recovery_page.click_eye_icon()
        assert recovery_page.check_display_password_visible()

    @allure.title('Проверка маскировки пароля в поле ввода после двух кликов на иконку с глазом')
    def test_double_click_on_eye_icon_makes_passwd_invisible_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button_main()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_recovery_password_page()
        recovery_page.send_keys_email()
        recovery_page.click_recovery_password_button()
        recovery_page.send_keys_password()
        recovery_page.click_eye_icon()
        recovery_page.click_eye_icon()
        assert recovery_page.check_display_password_invisible()