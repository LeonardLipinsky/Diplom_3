from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from locators.locators_main import LocatorsMain
import allure


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке перехода в личный кабинет в хэдере')
    def click_personal_account_header(self):
        self.wait_visibility_element(LocatorsMain.personal_account_button)
        self.click_element(LocatorsMain.personal_account_button)

    @allure.step('Клик по кнопке Лента заказов в хэдере')
    def click_header_feed_button(self):
        self.wait_visibility_element(LocatorsMain.order_feed_header_button)
        self.click_element(LocatorsMain.order_feed_header_button)

    @allure.step('Клик по кнопке Конструктор')
    def click_constructor_button(self):
        self.wait_visibility_element(LocatorsMain.header_constructor)
        self.click_element(LocatorsMain.header_constructor)

    @allure.step('Получение главного хедера конструктора')
    def get_text_header_constructor(self):
        return self.get_element_text(LocatorsMain.constructor_title)

    @allure.step('Клик по кнопке Войти в аккаунт на главной странице')
    def click_login_button_main(self):
        self.click_element(LocatorsMain.login_main_button)

    @allure.step('Проверить отображение окна создания заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        downloading = ActionChains(self.driver)
        downloading.pause(10) #Не получается справится увеличением времени visibility
        self.wait_visibility_element(LocatorsMain.confirmation_modal_order)
        return self.check_display_element(LocatorsMain.confirmation_modal_order)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.wait_visibility_element(LocatorsMain.ingredient_1)
        self.click_element(LocatorsMain.ingredient_1)

    @allure.step('Окно Детали ингредиента отображается')
    def check_detail_modal_display(self):
        self.wait_visibility_element(LocatorsMain.header_modal_details)
        return self.check_display_element(LocatorsMain.header_modal_details)

    @allure.step('Окно Детали ингредиента не отображается')
    def check_detail_modal_not_display(self):
        self.wait_close_element(LocatorsMain.header_modal_details)
        if not self.check_display_element(LocatorsMain.header_modal_details):
            return True

    @allure.step('Закрыть окно Детали ингредиента')
    def close_modal(self):
        self.wait_visibility_element(LocatorsMain.close_modal_button)
        self.click_element(LocatorsMain.close_modal_button)

    @allure.step('Добавить ингридиенты')
    def drag_and_drop_order_ingredient(self):
        source_element = self.find_element_with_wait(LocatorsMain.burger_ingredient)
        target_element = self.find_element_with_wait(LocatorsMain.place_for_ingredients)
        self.drag_and_drop(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_count_ingredients(self):
        return self.get_element_text(LocatorsMain.count_of_ingredient)

    @allure.step('Клик на кнопку создания заказа')
    def click_button_create_order(self):
        self.click_element(LocatorsMain.make_order_button)

    @allure.step('Проверить отображение создания заказа')
    def check_display_confirmation_modal(self):
        return self.check_display_element(LocatorsMain.confirmation_modal_order)

    @allure.step('Получить номер в окне создания заказа')
    def get_order_number_modal(self):
        self.wait_element_change_text(LocatorsMain.number_order_modal_confirmation, '9999')
        return self.get_element_text(LocatorsMain.number_order_modal_confirmation)

    @allure.step('Клик на кнопку закрытия окна создания заказа')
    def click_close_modal_button(self):
        self.check_element_clickable(LocatorsMain.close_confirmation_button)
        self.click_on_element_with_pause(LocatorsMain.close_confirmation_button)