from pages.base_page import BasePage
from locators.locators_recovery_password import LocatorsRecovery
from helpers import *
import allure


class RecoveryPasswordPage(BasePage):
    @allure.step('Открыть страницу восстановления пароля')
    def open_recovery_password_page(self):
        self.wait_visibility_element(LocatorsRecovery.FORGOT_PASSWORD_BUTTON)
        self.click_element(LocatorsRecovery.FORGOT_PASSWORD_BUTTON)

    @allure.step('Проверить отображение поля Email')
    def check_display_email_input(self):
        return self.check_display_element(LocatorsRecovery.EMAIL_INPUT)

    @allure.step('Проверить отображение поля Пароль')
    def check_display_password_input(self):
        self.wait_visibility_element(LocatorsRecovery.PASSWORD_INPUT)
        return self.check_display_element(LocatorsRecovery.PASSWORD_INPUT)

    @allure.step('Ввести email')
    def send_keys_email(self):
        self.wait_visibility_element(LocatorsRecovery.EMAIL_INPUT)
        email = create_random_email()
        self.send_keys_to_input(LocatorsRecovery.EMAIL_INPUT, email)

    @allure.step('Ввести пароль')
    def send_keys_password(self):
        self.wait_visibility_element(LocatorsRecovery.PASSWORD_INPUT)
        passwd = create_random_password()
        self.send_keys_to_input(LocatorsRecovery.PASSWORD_INPUT, passwd)

    @allure.step('Клик по кнопке Восстановить')
    def click_recovery_password_button(self):
        self.wait_visibility_element(LocatorsRecovery.RECOVERY_BUTTON)
        self.click_element(LocatorsRecovery.RECOVERY_BUTTON)

    @allure.step('Клик по иконке глаза')
    def click_eye_icon(self):
        self.wait_visibility_element(LocatorsRecovery.EYE_ICON)
        self.click_element(LocatorsRecovery.EYE_ICON)

    @allure.step('Проверить, что поле Пароль видимо')
    def check_display_password_visible(self):
        return self.check_display_element(LocatorsRecovery.PASSWORD_VISIBLE)

    @allure.step('Проверить, что поле Пароль невидимо')
    def check_display_password_invisible(self):
        return self.check_display_element(LocatorsRecovery.PASSWORD_INVISIBLE)