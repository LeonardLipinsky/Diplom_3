from selenium.webdriver.common.by import By


class LocatorsOrderHistory:

    order_title = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2') #Заголовок карточки заказа
    order_id = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]') #Номер заказа в карточке заказа
    order_card = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')  #Карточка заказа в истории заказов