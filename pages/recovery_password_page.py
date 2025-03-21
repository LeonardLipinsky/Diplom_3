from pages.base_page import BasePage
from locators.locators_recovery_password import LocatorsRecovery
from helpers import *
import allure


class RecoveryPasswordPage(BasePage):
    @allure.step('Открыть страницу восстановления пароля')
    def open_recovery_password_page(self):
        self.wait_visibility_element(LocatorsRecovery.forgot_password_button)
        self.click_element(LocatorsRecovery.forgot_password_button)

    @allure.step('Проверить отображение поля Email')
    def check_display_email_input(self):
        return self.check_display_element(LocatorsRecovery.email_input)

    @allure.step('Проверить отображение поля Пароль')
    def check_display_password_input(self):
        self.wait_visibility_element(LocatorsRecovery.password_input)
        return self.check_display_element(LocatorsRecovery.password_input)

    @allure.step('Ввести email')
    def send_keys_email(self):
        self.wait_visibility_element(LocatorsRecovery.email_input)
        email = create_random_email()
        self.send_keys_to_input(LocatorsRecovery.email_input, email)

    @allure.step('Ввести пароль')
    def send_keys_password(self):
        self.wait_visibility_element(LocatorsRecovery.password_input)
        passwd = create_random_password()
        self.send_keys_to_input(LocatorsRecovery.password_input, passwd)

    @allure.step('Клик по кнопке Восстановить')
    def click_recovery_password_button(self):
        self.wait_visibility_element(LocatorsRecovery.recovery_button)
        self.click_element(LocatorsRecovery.recovery_button)

    @allure.step('Клик по иконке глаза')
    def click_eye_icon(self):
        self.wait_visibility_element(LocatorsRecovery.eye_icon)
        self.click_element(LocatorsRecovery.eye_icon)

    @allure.step('Проверить, что поле Пароль видимо')
    def check_display_password_visible(self):
        return self.check_display_element(LocatorsRecovery.password_visible)

    @allure.step('Проверить, что поле Пароль невидимо')
    def check_display_password_invisible(self):
        return self.check_display_element(LocatorsRecovery.password_invisible)