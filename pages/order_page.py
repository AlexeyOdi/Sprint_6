import pytest
import locators.order_page_locators as opl
from selenium.webdriver.common.keys import Keys
import allure
from locators.order_page_locators import order_page_order_button, confirm_button, confirm_text
from pages.base_page import BasePage


@pytest.mark.usefixtures("get_driver")
class OrderPage(BasePage):

    names = ['Алексей', 'Ильшат']
    second_names = ['Алексеев', 'Ильшатов']
    addresses = ['Окружной проезд, вл2Ас1', '5-й проезд Подбельского, 4Ак5']
    metros = ['Черкизовская', 'Бульвар Рокоссовского']
    phones = ['89999999999', '+79999999999']
    comments = ['Помогите, мне трудно :D', 'Но надеюсь все будет хорошо']

    @allure.step('Задаем Имя')
    def set_name(self, name):
        self.send_keys(opl.name_input, name)

    @allure.step('Задаем фамилию')
    def set_second_name(self, second_name):
        self.send_keys(opl.sec_name_input, second_name)

    @allure.step('Задаем адрес')
    def set_address(self, address):
        self.send_keys(opl.address_input, address)

    @allure.step('Задаем метро')
    def set_metro(self, metro):
        self.send_keys(opl.metro_input, metro)
        self.send_keys(opl.metro_input, Keys.DOWN)
        self.send_keys(opl.metro_input, Keys.ENTER)

    @allure.step('Задаем номер телефона')
    def set_phone(self, phone):
        self.send_keys(opl.phone_input, phone)

    @allure.step('Кликаем кнопку далее на странице заказа чтобы продолжить оформление')
    def click_next_button(self):
        self.click(opl.next_button)

    @allure.step('Задаем дату доставки')
    def set_date(self):
        self.click(opl.date_input)
        self.send_keys(opl.date_input, Keys.DOWN)
        self.send_keys(opl.date_input, Keys.ENTER)

    @allure.step('Задаем время аренды')
    def set_rental_period(self):
        self.click(opl.rental_period_input)
        self.click(opl.day_period)

    @allure.step('Задаем цвет самоката')
    def set_black_color(self):
        self.click(opl.color_label_black)

    @allure.step('Задаем комментарий')
    def set_comment(self, comment):
        self.send_keys(opl.comment_input, comment)

    @allure.step('Кликаем кнопку "Заказа" чтобы оформить заказ')
    def click_order_page_order_button(self):
        self.click(order_page_order_button)

    @allure.step('Кликаем кнопку "Да" чтобы подтвердить оформление заказа')
    def click_confirm(self):
        self.click(opl.confirm_button)

    @allure.step('Получаем текст подтверждения')
    def get_confirm_text(self):
        return self.get_text(confirm_text)

    @allure.step('Проверяем что заказ подтвердился')
    def check_assert_order_is_confirmed(self, test_value):
        assert "Заказ оформлен" in test_value


