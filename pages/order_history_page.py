from locators.locators_order_history import LocatorsOrderHistory
from pages.base_page import BasePage
import allure


class OrderHistoryPage(BasePage):

    @allure.step('Ожидание карточки заказа')
    def wait_order_visibility(self):
        self.wait_visibility_element(LocatorsOrderHistory.order_card)

    @allure.step('Получить текст заказа')
    def get_text_order_card_header(self):
        return self.get_element_text(LocatorsOrderHistory.order_title)

    @allure.step('Получить номер заказа в карточке')
    def get_id_order_card(self):
        return self.get_element_text(LocatorsOrderHistory.order_card)