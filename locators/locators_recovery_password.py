from selenium.webdriver.common.by import By


class LocatorsRecovery:
    RECOVERY_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0') #Восстановить
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[text() = "Восстановить пароль"]')  #Восстановить пароль
    EMAIL_INPUT = (By.CLASS_NAME, 'input__textfield')  #Поле ввода email
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.input_type_password .input__textfield') #Поле ввода пароля
    EYE_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]') #Иконка скрытия пароля
    PASSWORD_VISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                          '"input_status_active")]') #Пароль виден
    PASSWORD_INVISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                             '"input_type_password")]') #Пароль не виден