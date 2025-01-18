from pages.main_page import MainPage
import pytest
import allure

@pytest.mark.usefixtures("get_driver_function")
class TestMainPage:

    @allure.title('Проверка нажатия на логотип яндекса')
    def test_ya_logo(self):

        test_main = MainPage(self.driver)
        test_main.click_header_order()
        test_main.click_ya_logo()
        test_main.check_assert_ya_logo()

    @allure.title('Проверка нажатия на логотип самоката')
    def test_scooter_logo(self):

        test_main = MainPage(self.driver)
        test_main.click_header_order()
        test_main.click_scooter_logo()
        test_main.check_assert_scooter_logo()

    @allure.title('Проверка нажатия на кнопку "Заказать" в шапке страницы')
    def test_header_order_button(self):

        test_main = MainPage(self.driver)
        test_main.click_header_order()
        test_main.check_assert_order_page()

    @allure.title('Проверка нажатия на кнопку "Заказать" центре странице')
    def test_home_order_button(self):

        test_main = MainPage(self.driver)
        test_main.scroll_to_home_order_button()
        test_main.click_home_order_button()
        test_main.check_assert_order_page()





