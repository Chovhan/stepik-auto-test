import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/"


def test_check_add_to_basket_button_on_page(browser):
    button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='add_to_basket_form']/button"))
    )
    # Add "time.sleep(5), to see the result and make sure that the browser is running in the correct language
    # and the web-site is displayed in the language in which the browser is running
    time.sleep(30)
    assert len(str(button)) != 0, "Can`t find 'Add to basket' button on page!"


