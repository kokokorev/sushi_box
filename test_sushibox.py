from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_add_item_to_basket():
    # Перейти на главную страницу SushiBox
    driver.get('https://ulyanovsk.sushibox.org/')
    try:
        driver.find_element(by=By.XPATH, value="//button[contains(@class, 'CityQuestion_cityQuestion__button__')]").click()
    except:
        pass
    # Нажать на первую категорию товаров
    driver.find_element(by=By.CLASS_NAME, value='catalog__product').click()
    # Нажать кнопку "В корзину" у первого товара
    driver.find_element(by=By.CLASS_NAME, value='basic__button').click()
    # Перейти в корзину
    driver.find_elements(by=By.XPATH, value="//a[@href='/cart']")[1].click()
    #   Товар находится в Корзине
    assert driver.find_element(by=By.CLASS_NAME, value='product-box').is_displayed()
    
    driver.find_element(by=By.CLASS_NAME, value='cart__icon-trash_bin').click()


def test_delete_item_from_basket():
    # Перейти на главную страницу SushiBox
    driver.get('https://ulyanovsk.sushibox.org/')
    try:
        driver.find_element(by=By.XPATH, value="//button[contains(@class, 'CityQuestion_cityQuestion__button__')]").click()
    except:
        pass
    # Нажать на первую категорию товаров
    driver.find_element(by=By.CLASS_NAME, value='catalog__product').click()
    # Нажать кнопку "В корзину" у первого товара
    driver.find_element(by=By.CLASS_NAME, value='basic__button').click()
    # Перейти в корзину
    driver.find_elements(by=By.XPATH, value="//a[@href='/cart']")[1].click()
    # Нажать кнопку удаления товара из Корзины
    driver.find_element(by=By.CLASS_NAME, value='cart__icon-trash_bin').click()
    #   Корзина пустая
    assert driver.find_element(by=By.CLASS_NAME, value='cart__empty').is_displayed()


def test_increasing_item_in_basket():
    # Перейти на главную страницу SushiBox
    driver.get('https://ulyanovsk.sushibox.org/')
    try:
        driver.find_element(by=By.XPATH, value="//button[contains(@class, 'CityQuestion_cityQuestion__button__')]").click()
    except:
        pass
    # Нажать на первую категорию товаров
    driver.find_element(by=By.CLASS_NAME, value='catalog__product').click()
    # Нажать кнопку "В корзину" у первого товара
    driver.find_element(by=By.CLASS_NAME, value='basic__button').click()
    # Перейти в корзину
    driver.find_elements(by=By.XPATH, value="//a[@href='/cart']")[1].click()
    # Нажать кнопку увеличения количества товара в Корзине
    driver.find_elements(by=By.CLASS_NAME, value='counter')[1].click()
    #   Счетчик количества товара увеличивается и равен 2
    assert driver.find_element(by=By.CLASS_NAME, value='count').text == '2'
    
    driver.find_element(by=By.CLASS_NAME, value='cart__icon-trash_bin').click()


def test_reduce_item_in_basket():
    # Перейти на главную страницу SushiBox
    driver.get('https://ulyanovsk.sushibox.org/')
    try:
        driver.find_element(by=By.XPATH, value="//button[contains(@class, 'CityQuestion_cityQuestion__button__')]").click()
    except:
        pass
    # Нажать на первую категорию товаров
    driver.find_element(by=By.CLASS_NAME, value='catalog__product').click()
    # Нажать кнопку "В корзину" у первого товара
    driver.find_element(by=By.CLASS_NAME, value='basic__button').click()
    # Перейти в корзину
    driver.find_elements(by=By.XPATH, value="//a[@href='/cart']")[1].click()
    # Нажать кнопку увеличения количества товара в Корзине
    driver.find_elements(by=By.CLASS_NAME, value='counter')[1].click()
    # Нажать кнопку уменьшения количества товара в Корзине
    driver.find_elements(by=By.CLASS_NAME, value='counter')[0].click()
    #   Счетчик количества товара уменьшается и равен 1
    assert driver.find_element(by=By.CLASS_NAME, value='count').text == '1'
    
    driver.find_element(by=By.CLASS_NAME, value='cart__icon-trash_bin').click()
    print('[test_reduce_item_in_basket() passed]\n')


def test_teardown():
    driver.close()
    driver.quit()
