from selenium.webdriver.common.by import By


class LocatorsMain:

    header_constructor = (By.XPATH, '//p[text() = "Конструктор"]') #Конструктор
    header_modal_details = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')  # Хедер Детали ингредиента
    constructor_title = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1') #Хедер Конструктор
    buns_block = (By.XPATH, '//span[text() = "Булки"]') #Хедер Булки
    sauces = (By.XPATH, '//span[text() = "Соусы"]') #Хедер Соусы
    fillings = (By.XPATH, '//span[text() = "Начинки"]') #Хедер Начинки
    ingredient_1 = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]') #Ингредиент
    close_modal_button = (By.XPATH, '//section[contains(@class, '
                                    '"Modal_modal_opened")]//button[contains(@class, "close")]') #Крестик Детали ингредиента
    personal_account_button = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a') #Личный кабинет
    order_feed_header_button = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li') #Лента заказов
    make_order_by_text = (By.XPATH, '//button[text()="Оформить заказ"]')  # Оформить заказ текст
    login_main_button = By.XPATH, './/button[text() = "Войти в аккаунт"]'  # Войти в аккаунт
    close_confirmation_button = (By.XPATH, "(//button[contains(@class, 'close_modified')])[1]") #Кнопка с крестиком
    make_order_button = (By.CLASS_NAME, 'button_button__33qZ0') #Оформить заказ
    button_select = (By.XPATH, ('//div[@class = '
                                  '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')) #Раздел конструктора
    place_for_ingredients = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]') #Корзина ингредиентов
    content_of_order = (By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row') #Список Корзины
    burger_ingredient = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]') #Изображение ингредиента
    confirmation_modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]') #Окно создания заказа
    number_order_modal_confirmation = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2') #Номер заказа
    count_of_ingredient = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                     '@class="counter_counter__num__3nue1"][1]') #Количество ингредиента в заказе