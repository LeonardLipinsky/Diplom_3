from selenium.webdriver.common.by import By


class LocatorsFeed:

    orders_list = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]') #Заказы
    name_feed_order = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1') #Заголовок ленты заказов
    feed_order = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]') #Заказ в ленте
    name_modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2') #Заголовок всплывающего окна с деталями заказа
    modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')  #Всплывающее окно с деталями заказа
    quantity_order = (By.XPATH, '//p[normalize-space(text())="Выполнено за все время:"]/following-sibling::p') #Счетчик заказов за всё время
    daily_quantity_order = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p') #Счетчик заказов за сегодня
    order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li') #Заказ в работе
    quantity_order_in_progress = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]') #Номер заказа в работе
    id_order_card = (By.XPATH, './/*[text()="{order_id}"]') #Номер заказа в ленте