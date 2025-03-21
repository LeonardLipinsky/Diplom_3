from selenium.webdriver.common.by import By


class LocatorsRecovery:
    recovery_button = (By.CLASS_NAME, 'button_button__33qZ0') #Восстановить
    forgot_password_button = (By.XPATH, '//a[text() = "Восстановить пароль"]')  #Восстановить пароль
    email_input = (By.CLASS_NAME, 'input__textfield')  #Поле ввода email
    password_input = (By.CSS_SELECTOR, '.input_type_password .input__textfield') #Поле ввода пароля
    eye_icon = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]') #Иконка скрытия пароля
    password_visible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                          '"input_status_active")]') #Пароль виден
    password_invisible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                             '"input_type_password")]') #Пароль не виден