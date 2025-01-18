import pytest
import locators.order_page_locators as opl
from selenium.webdriver.common.keys import Keys
import allure
from locators.order_page_locators import order_page_order_button, confirm_button, confirm_text

@pytest.mark.usefixtures("get_driver")
class OrderPage:

    names = ['Алексей', 'Ильшат']
    second_names = ['Алексеев', 'Ильшатов']
    addresses = ['Окружной проезд, вл2Ас1', '5-й проезд Подбельского, 4Ак5']
    metros = ['Черкизовская', 'Бульвар Рокоссовского']
    phones = ['89999999999', '+79999999999']
    comments = ['Помогите, мне трудно :D', 'Но надеюсь все будет хорошо']

    @allure.step('Инициализируем веб-драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Задаем Имя')
    def set_name(self, name):
        self.driver.find_element(*opl.name_input).send_keys(name)

    @allure.step('Задаем фамилию')
    def set_second_name(self, second_name):
        self.driver.find_element(*opl.sec_name_input).send_keys(second_name)

    @allure.step('Задаем адрес')
    def set_address(self, address):
        self.driver.find_element(*opl.address_input).send_keys(address)

    @allure.step('Задаем метро')
    def set_metro(self, metro):
        self.driver.find_element(*opl.metro_input).send_keys(metro)
        self.driver.find_element(*opl.metro_input).send_keys(Keys.DOWN)
        self.driver.find_element(*opl.metro_input).send_keys(Keys.ENTER)

    @allure.step('Задаем номер телефона')
    def set_phone(self, phone):
        self.driver.find_element(*opl.phone_input).send_keys(phone)

    @allure.step('Кликаем кнопку далее на странице заказа чтобы продолжить оформление')
    def click_next_button(self):
        self.driver.find_element(*opl.next_button).click()

    @allure.step('Задаем дату доставки')
    def set_date(self):
        self.driver.find_element(*opl.date_input).click()
        self.driver.find_element(*opl.date_input).send_keys(Keys.DOWN)
        self.driver.find_element(*opl.date_input).send_keys(Keys.ENTER)

    @allure.step('Задаем время аренды')
    def set_rental_period(self):
        self.driver.find_element(*opl.rental_period_input).click()
        self.driver.find_element(*opl.day_period).click()

    @allure.step('Задаем цвет самоката')
    def set_black_color(self):
        self.driver.find_element(*opl.color_label_black).click()

    @allure.step('Задаем комментарий')
    def set_comment(self, comment):
        self.driver.find_element(*opl.comment_input).send_keys(comment)

    @allure.step('Кликаем кнопку "Заказа" чтобы оформить заказ')
    def click_order_page_order_button(self):
        self.driver.find_element(*order_page_order_button).click()

    @allure.step('Кликаем кнопку "Да" чтобы подтвердить оформление заказа')
    def click_confirm(self):
        self.driver.find_element(*opl.confirm_button).click()

    @allure.step('Получаем текст подтверждения')
    def get_confirm_text(self):
        return self.driver.find_element(*confirm_text).text

    @allure.step('Проверяем что заказ подтвердился')
    def check_assert_order_is_confirmed(self, test_value):
        assert "Заказ оформлен" in test_value


