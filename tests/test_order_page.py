import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import phone_input
from pages.main_page import MainPage
import urls
import pytest
import locators.base_page_locators as bpl
import locators.order_page_locators as opl
from pages.order_page import OrderPage


class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('name, second_name, address, metro, phone, comment',
                             [[OrderPage.names[0], OrderPage.second_names[0], OrderPage.addresses[0], OrderPage.metros[0], OrderPage.phones[0], OrderPage.comments[0]],
                              [OrderPage.names[1], OrderPage.second_names[1], OrderPage.addresses[1], OrderPage.metros[1], OrderPage.phones[1], OrderPage.comments[1]]
                              ])
    def test_order(self, name, second_name, address, metro, phone, comment):

        self.driver.get(urls.main_page)
        test_main_page = MainPage(self.driver)
        test_order_page = OrderPage(self.driver)
        test_main_page.click_header_order()
        test_order_page.set_name(name)
        test_order_page.set_second_name(second_name)
        test_order_page.set_address(address)
        test_order_page.set_metro(metro)
        test_order_page.wait_for_phone_input()
        test_order_page.set_phone(phone)
        test_order_page.click_next_button()
        test_order_page.set_date()
        test_order_page.set_rental_period()
        test_order_page.set_black_color()
        test_order_page.set_comment(comment)
        test_order_page.click_order_page_order_button()
        test_order_page.click_confirm()
        test_value = test_order_page.get_confirm_text()
        assert "Заказ оформлен" in test_value

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()