import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_cart_button(browser):
    browser.get(link)
   
    time.sleep(10) # можно увеличить время задержки для проверки
    buttons_count = len(browser.find_elements(By.XPATH, "//*[@class='tn btn-lg btn-primary btn-add-to-basket']")) #  возвращает количество элементов
    assert buttons_count > 0, "The button not found!"
    if buttons_count > 0: # если кнопка есть, выводится название кнопки
        button_text = browser.find_element(By.XPATH, "//*[@class='btn btn-lg btn-primary btn-add-to-basket']").text
        print(f"Button text is '{button_text}'")

