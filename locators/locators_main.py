from selenium.webdriver.common.by import By


class LocatorsMain:

    HEADER_CONSTRUCTOR = (By.XPATH, '//p[text() = "Конструктор"]') #Конструктор
    HEADER_MODAL_DETAILS = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')  # Хедер Детали ингредиента
    CONSTRUCTOR_TITLE = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1') #Хедер Конструктор
    BUNS_BLOCK = (By.XPATH, '//span[text() = "Булки"]') #Хедер Булки
    SAUCES = (By.XPATH, '//span[text() = "Соусы"]') #Хедер Соусы
    FILLINGS = (By.XPATH, '//span[text() = "Начинки"]') #Хедер Начинки
    INGREDIENT_1 = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]') #Ингредиент
    CLOSE_MODAL_BUTTON = (By.XPATH, '//section[contains(@class, '
                                    '"Modal_modal_opened")]//button[contains(@class, "close")]') #Крестик Детали ингредиента
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a') #Личный кабинет
    ORDER_FEED_HEADER_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li') #Лента заказов
    MAKE_ORDER_BY_TEXT = (By.XPATH, '//button[text()="Оформить заказ"]')  # Оформить заказ текст
    LOGIN_MAIN_BUTTON = By.XPATH, './/button[text() = "Войти в аккаунт"]'  # Войти в аккаунт
    CLOSE_CONFIRMATION_BUTTON = (By.XPATH, "(//button[contains(@class, 'close_modified')])[1]") #Кнопка с крестиком
    MAKE_ORDER_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0') #Оформить заказ
    BUTTON_SELECT = (By.XPATH, ('//div[@class = '
                                  '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')) #Раздел конструктора
    PLACE_FOR_INGREDIENTS = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]') #Корзина ингредиентов
    CONTENT_OF_ORDER = (By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row') #Список Корзины
    BURGER_INGREDIENT = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]') #Изображение ингредиента
    CONFIRMATION_MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]') #Окно создания заказа
    NUMBER_ORDER_MODAL_CONFIRMATION = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2') #Номер заказа
    COUNT_OF_INGREDIENT = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                     '@class="counter_counter__num__3nue1"][1]') #Количество ингредиента в заказе