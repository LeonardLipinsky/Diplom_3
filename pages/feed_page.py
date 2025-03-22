from pages.base_page import BasePage
from locators.locators_feed import LocatorsFeed
import allure


class FeedPage(BasePage):
    @allure.step('Получить текст хедера заказов')
    def get_text_title_order_list(self):
        return self.get_element_text(LocatorsFeed.NAME_FEED_ORDER)

    @allure.step('Кликнуть по первому (последнему) заказу в ленте')
    def click_order(self):
        self.wait_visibility_element(LocatorsFeed.FEED_ORDER)
        self.click_element(LocatorsFeed.FEED_ORDER)

    @allure.step('Получить текст хедера окна с деталями заказа')
    def get_text_header_modal_order(self):
        return self.get_element_text(LocatorsFeed.NAME_MODAL_ORDER)

    @allure.step('Получить заказы за сегодня')
    def get_daily_quantity_order(self):
        self.find_element_with_wait(LocatorsFeed.DAILY_QUANTITY_ORDER)
        return self.get_element_text(LocatorsFeed.DAILY_QUANTITY_ORDER)

    @allure.step('Получить заказы за всё время')
    def get_quantity_orders(self):
        self.find_element_with_wait(LocatorsFeed.QUANTITY_ORDER)
        return self.get_element_text(LocatorsFeed.QUANTITY_ORDER)

    @allure.step('Проверить существование id заказа в ленте')
    def check_id_order_feed(self, order_id):
        locator = LocatorsFeed.ID_ORDER_CARD
        locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        self.find_element_with_wait(locator_with_order_id)
        return self.check_display_element(locator_with_order_id)

    @allure.step('Получить id последнего заказа В работе')
    def get_order_id_feed_progress(self):
        return self.get_element_text(LocatorsFeed.QUANTITY_ORDER_IN_PROGRESS)