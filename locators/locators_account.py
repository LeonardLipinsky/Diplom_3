from selenium.webdriver.common.by import By


class LocatorsAccount:

    profile_link = (By.XPATH, '//a[@href = "/account/profile"]') #Профиль
    register_button = By.XPATH, '//a[text() = "Зарегистрироваться"]' #Зарегистрироваться
    hint_of_section = (By.XPATH, '//p[contains(@class, "Account_text")]') #текстовая подсказка
    exit_button = (By.XPATH, '//button[@type = "button"]') #выход
    order_history = (By.XPATH, '//a[@href = "/account/order-history"]') #история заказов