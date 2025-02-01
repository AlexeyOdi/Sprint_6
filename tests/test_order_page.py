from pages.main_page import MainPage
import pytest
from pages.order_page import OrderPage
import allure

@pytest.mark.usefixtures("get_driver_function")
class TestOrderPage:

    @allure.title("Проверяем оформление заказа")
    @pytest.mark.parametrize('name, second_name, address, metro, phone, comment',
                             [[OrderPage.names[0], OrderPage.second_names[0], OrderPage.addresses[0], OrderPage.metros[0], OrderPage.phones[0], OrderPage.comments[0]],
                              [OrderPage.names[1], OrderPage.second_names[1], OrderPage.addresses[1], OrderPage.metros[1], OrderPage.phones[1], OrderPage.comments[1]]
                              ])
    def test_order(self, name, second_name, address, metro, phone, comment):

        test_main_page = MainPage(self.driver)
        test_order_page = OrderPage(self.driver)
        test_main_page.click_header_order()
        test_order_page.set_name(name)
        test_order_page.set_second_name(second_name)
        test_order_page.set_address(address)
        test_order_page.set_metro(metro)
        test_order_page.set_phone(phone)
        test_order_page.click_next_button()
        test_order_page.set_date()
        test_order_page.set_rental_period()
        test_order_page.set_black_color()
        test_order_page.set_comment(comment)
        test_order_page.click_order_page_order_button()
        test_order_page.click_confirm()
        test_value = test_order_page.get_confirm_text()
        test_order_page.check_assert_order_is_confirmed(test_value)