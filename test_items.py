import time


def test_button_add_to_basket_present(browser):
    """Проверяет, что на странице товара есть кнопка добавления в корзину"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    button = browser.find_element(
        "css selector", "button.btn-add-to-basket"
    )

    assert button is not None, \
        "Кнопка добавления в корзину не найдена на странице товара"