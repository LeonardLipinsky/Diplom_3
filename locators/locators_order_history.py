from selenium.webdriver.common.by import By


class LocatorsOrderHistory:

    ORDER_TITLE = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2') #Заголовок карточки заказа
    ORDER_ID = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]') #Номер заказа в карточке заказа
    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')  #Карточка заказа в истории заказов