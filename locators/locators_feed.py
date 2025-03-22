from selenium.webdriver.common.by import By


class LocatorsFeed:

    ORDERS_LIST = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]') #Заказы
    NAME_FEED_ORDER = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1') #Заголовок ленты заказов
    FEED_ORDER = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]') #Заказ в ленте
    NAME_MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2') #Заголовок всплывающего окна с деталями заказа
    MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')  #Всплывающее окно с деталями заказа
    QUANTITY_ORDER = (By.XPATH, '//p[normalize-space(text())="Выполнено за все время:"]/following-sibling::p') #Счетчик заказов за всё время
    DAILY_QUANTITY_ORDER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p') #Счетчик заказов за сегодня
    ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li') #Заказ в работе
    QUANTITY_ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]') #Номер заказа в работе
    ID_ORDER_CARD = (By.XPATH, './/*[text()="{order_id}"]') #Номер заказа в ленте