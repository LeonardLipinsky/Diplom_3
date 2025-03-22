import time

from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from locators.locators_main import LocatorsMain
import allure


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке перехода в личный кабинет в хэдере')
    def click_personal_account_header(self):
        self.wait_visibility_element(LocatorsMain.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(LocatorsMain.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке Лента заказов в хэдере')
    def click_header_feed_button(self):
        self.wait_visibility_element(LocatorsMain.ORDER_FEED_HEADER_BUTTON)
        self.click_element(LocatorsMain.ORDER_FEED_HEADER_BUTTON)

    @allure.step('Клик по кнопке Конструктор')
    def click_constructor_button(self):
        self.wait_visibility_element(LocatorsMain.HEADER_CONSTRUCTOR)
        self.click_element(LocatorsMain.HEADER_CONSTRUCTOR)

    @allure.step('Получение главного хедера конструктора')
    def get_text_header_constructor(self):
        return self.get_element_text(LocatorsMain.CONSTRUCTOR_TITLE)

    @allure.step('Клик по кнопке Войти в аккаунт на главной странице')
    def click_login_button_main(self):
        self.click_element(LocatorsMain.LOGIN_MAIN_BUTTON)

    @allure.step('Проверить отображение окна создания заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        downloading = ActionChains(self.driver)
        downloading.pause(10) #Не получается справится увеличением времени visibility
        self.wait_visibility_element(LocatorsMain.CONFIRMATION_MODAL_ORDER)
        return self.check_display_element(LocatorsMain.CONFIRMATION_MODAL_ORDER)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.wait_visibility_element(LocatorsMain.INGREDIENT_1)
        self.click_element(LocatorsMain.INGREDIENT_1)

    @allure.step('Окно Детали ингредиента отображается')
    def check_detail_modal_display(self):
        self.wait_visibility_element(LocatorsMain.HEADER_MODAL_DETAILS)
        return self.check_display_element(LocatorsMain.HEADER_MODAL_DETAILS)

    @allure.step('Окно Детали ингредиента не отображается')
    def check_detail_modal_not_display(self):
        self.wait_close_element(LocatorsMain.HEADER_MODAL_DETAILS)
        if not self.check_display_element(LocatorsMain.HEADER_MODAL_DETAILS):
            return True

    @allure.step('Закрыть окно Детали ингредиента')
    def close_modal(self):
        self.wait_visibility_element(LocatorsMain.CLOSE_MODAL_BUTTON)
        self.click_element(LocatorsMain.CLOSE_MODAL_BUTTON)

    @allure.step('Добавить ингридиенты')
    def drag_and_drop_order_ingredient(self):
        source_element = self.find_element_with_wait(LocatorsMain.BURGER_INGREDIENT)
        target_element = self.find_element_with_wait(LocatorsMain.PLACE_FOR_INGREDIENTS)
        self.drag_and_drop(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_count_ingredients(self):
        return self.get_element_text(LocatorsMain.COUNT_OF_INGREDIENT)

    @allure.step('Клик на кнопку создания заказа')
    def click_button_create_order(self):
        self.click_element(LocatorsMain.MAKE_ORDER_BUTTON)

    @allure.step('Проверить отображение создания заказа')
    def check_display_confirmation_modal(self):
        downloading = ActionChains(self.driver)
        downloading.pause(5).perform()
        return self.check_display_element(LocatorsMain.CONFIRMATION_MODAL_ORDER)

    @allure.step('Получить номер в окне создания заказа')
    def get_order_number_modal(self):
        downloading = ActionChains(self.driver)
        downloading.pause(5).perform()
        self.wait_element_change_text(LocatorsMain.NUMBER_ORDER_MODAL_CONFIRMATION, '9999')
        return self.get_element_text(LocatorsMain.NUMBER_ORDER_MODAL_CONFIRMATION)

    @allure.step('Клик на кнопку закрытия окна создания заказа')
    def click_close_modal_button(self):
        self.check_element_clickable(LocatorsMain.CLOSE_CONFIRMATION_BUTTON)
        self.click_on_element_with_pause(LocatorsMain.CLOSE_CONFIRMATION_BUTTON)