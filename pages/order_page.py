import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import urls
import locators.order_page_locators as opl
import locators.base_page_locators as bpl
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import order_page_order_button, confirm_button, confirm_text


class OrderPage:

    driver = None

    names = ['Алексей', 'Ильшат']
    second_names = ['Алексеев', 'Ильшатов']
    addresses = ['Окружной проезд, вл2Ас1', '5-й проезд Подбельского, 4Ак5']
    metros = ['Черкизовская', 'Бульвар Рокоссовского']
    phones = ['89999999999', '+79999999999']
    comments = ['Помогите, мне трудно :D', 'Но надеюсь все будет хорошо']

    #@allure.step('Инициализируем веб-драйвер')
    def __init__(self, driver):
        self.driver = driver

    #@allure.step('Задаем Имя')
    def set_name(self, name):
        self.driver.find_element(*opl.name_input).send_keys(name)

    #@allure.step('Задаем фамилию')
    def set_second_name(self, second_name):
        self.driver.find_element(*opl.sec_name_input).send_keys(second_name)

    #@allure.step('Задаем адрес')
    def set_address(self, address):
        self.driver.find_element(*opl.address_input).send_keys(address)

    #@allure.step('Задаем метро')
    def set_metro(self, metro):
        self.driver.find_element(*opl.metro_input).send_keys(metro)
        self.driver.find_element(*opl.metro_input).send_keys(Keys.DOWN)
        self.driver.find_element(*opl.metro_input).send_keys(Keys.ENTER)

    #@allure.step('Задаем номер телефона')
    def set_phone(self, phone):
        self.driver.find_element(*opl.phone_input).send_keys(phone)

    #@allure.step('Кликаем кнопку далее на странице заказа чтобы продолжить оформление')
    def click_next_button(self):
        self.driver.find_element(*opl.next_button).click()

    #@allure.step('Задаем дату доставки')
    def set_date(self):
        self.driver.find_element(*opl.date_input).click()
        self.driver.find_element(*opl.date_input).send_keys(Keys.DOWN)
        self.driver.find_element(*opl.date_input).send_keys(Keys.ENTER)

    #@allure.step('Задаем время аренды')
    def set_rental_period(self):
        self.driver.find_element(*opl.rental_period_input).click()
        self.driver.find_element(*opl.day_period).click()

    #@allure.step('Задаем цвет самоката')
    def set_black_color(self):
        self.driver.find_element(*opl.color_label_black).click()

    #@allure.step('Задаем комментарий')
    def set_comment(self, comment):
        self.driver.find_element(*opl.comment_input).send_keys(comment)

    #@allure.step('Кликаем кнопку "Заказа" чтобы оформить заказ')
    def click_order_page_order_button(self):
        self.driver.find_element(*order_page_order_button).click()

    #@allure.step('Кликаем кнопку "Да" чтобы подтвердить оформление заказа')
    def click_confirm(self):
        self.driver.find_element(*confirm_button).click()

    #@allure.step('Получаем текст подтверждения')
    def get_confirm_text(self):
        return self.driver.find_element(*confirm_text).text

    #@allure.step('Ожидаем появление поля для ввода номера телефона в зоне видимости')
    def wait_for_phone_input(self):
        element = self.driver.find_element(*opl.phone_input)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of((element)))

