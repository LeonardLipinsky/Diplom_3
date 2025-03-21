from pages.base_page import BasePage
from locators.locators_account import LocatorsAccount
import allure


class AccountPage(BasePage):
    @allure.step('Клик по кнопке История заказов')
    def click_order_history_button(self):
        self.click_element(LocatorsAccount.order_history)

    @allure.step('Клик по кнопке Выйти')
    def click_exit_button(self):
        self.click_element(LocatorsAccount.exit_button)

    @allure.step('Ожидание видимости описания раздела')
    def wait_description_visibility(self):
        self.wait_visibility_element(LocatorsAccount.hint_of_section)

    @allure.step('Проверить отображение описания раздела')
    def check_display_description(self):
        return self.check_display_element(LocatorsAccount.hint_of_section)

    @allure.step('Ожидание видимости кнопки Зарегистрироваться')
    def wait_register_button_visibility(self):
        self.wait_visibility_element(LocatorsAccount.register_button)

    @allure.step('Проверить отображение кнопки Зарегистрироваться')
    def check_display_register_button(self):
        return self.check_display_element(LocatorsAccount.register_button)