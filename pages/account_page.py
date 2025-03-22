from pages.base_page import BasePage
from locators.locators_account import LocatorsAccount
import allure


class AccountPage(BasePage):
    @allure.step('Клик по кнопке История заказов')
    def click_order_history_button(self):
        self.click_element(LocatorsAccount.ORDER_HISTORY)

    @allure.step('Клик по кнопке Выйти')
    def click_exit_button(self):
        self.click_element(LocatorsAccount.EXIT_BUTTON)

    @allure.step('Ожидание видимости описания раздела')
    def wait_description_visibility(self):
        self.wait_visibility_element(LocatorsAccount.HINT_OF_SECTION)

    @allure.step('Проверить отображение описания раздела')
    def check_display_description(self):
        return self.check_display_element(LocatorsAccount.HINT_OF_SECTION)

    @allure.step('Ожидание видимости кнопки Зарегистрироваться')
    def wait_register_button_visibility(self):
        self.wait_visibility_element(LocatorsAccount.REGISTER_BUTTON)

    @allure.step('Проверить отображение кнопки Зарегистрироваться')
    def check_display_register_button(self):
        return self.check_display_element(LocatorsAccount.REGISTER_BUTTON)