from selenium.webdriver.common.by import By


class LocatorsAccount:

    PROFILE_LINK = (By.XPATH, '//a[@href = "/account/profile"]') #Профиль
    REGISTER_BUTTON = By.XPATH, '//a[text() = "Зарегистрироваться"]' #Зарегистрироваться
    HINT_OF_SECTION = (By.XPATH, '//p[contains(@class, "Account_text")]') #текстовая подсказка
    EXIT_BUTTON = (By.XPATH, '//button[@type = "button"]') #выход
    ORDER_HISTORY = (By.XPATH, '//a[@href = "/account/order-history"]') #история заказов