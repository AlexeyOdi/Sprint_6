from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urls
import locators.base_page_locators as bpl
import allure

from pages.base_page import BasePage


class MainPage(BasePage):

    question_1 = [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div']
    answer_1 = [By.XPATH, '//div[@id="accordion__panel-0"]']
    answer_text_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    question_2 = [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div']
    answer_2 = [By.XPATH, '//div[@id="accordion__panel-1"]']
    answer_text_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    question_3 = [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div']
    answer_3 = [By.XPATH, '//div[@id="accordion__panel-2"]']
    answer_text_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    question_4 = [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div']
    answer_4 = [By.XPATH, '//div[@id="accordion__panel-3"]']
    answer_text_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    question_5 = [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div']
    answer_5 = [By.XPATH, '//div[@id="accordion__panel-4"]']
    answer_text_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    question_6 = [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div']
    answer_6 = [By.XPATH, '//div[@id="accordion__panel-5"]']
    answer_text_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    question_7 = [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div']
    answer_7 = [By.XPATH, '//div[@id="accordion__panel-6"]']
    answer_text_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    question_8 = [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div']
    answer_8 = [By.XPATH, '//div[@id="accordion__panel-7"]']
    answer_text_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @allure.step('Кликаем на вопрос')
    def click_question(self, question):
        self.click(question)

    @allure.step('Получаем текст фактического ответа')
    def get_answer_text(self, answer):
        return self.get_text(answer)

    @allure.step('Прокручиваем страницу до самого низа')
    def sroll_to_down(self):
        self.scroll_to_down()

    @allure.step('Прокручиваем страницу до кнопки "заказать" в середине страницы')
    def scroll_to_home_order_button(self):
        self.scroll_to(bpl.home_order_button)

    @allure.step('Получаем текст ожидаемого ответа')
    def get_text_to_assert(self, answer_text):
        return answer_text

    @allure.step('Кликаем на кнопку "заказать" в шапке страницы')
    def click_header_order(self):
        self.click(bpl.header_order_button)

    @allure.step('Кликаем лого самоката')
    def click_scooter_logo(self):
        self.click(bpl.scooter_logo)

    @allure.step('Кликаем лого Яндекс')
    def click_ya_logo(self):
        self.click(bpl.ya_logo)

    @allure.step('Кликаем кнопку "заказать" в середине страницы')
    def click_home_order_button(self):
        self.click(bpl.home_order_button)

    @allure.step('Сравниваем полученный текст ответа с ожидаемым')
    def assert_answers(self, expected_value, actual_value):
        assert expected_value == actual_value

    @allure.step('Проверяем, что после клика мы перешли на главную страницу самоката')
    def check_assert_scooter_logo(self):
        assert self.get_current_url() == urls.main_page

    @allure.step('Проверяем, что после клика мы перешли на страницу оформления заказа')
    def check_assert_order_page(self):
        assert self.get_current_url() == urls.order_page

    @allure.step('Проверяем, что после клика мы перешли на страницу Яндекс.Дзен')
    def check_assert_ya_logo(self):
        main_window_handler = self.get_current_window_handle()
        for window_handle in self.get_window_handles():
            if window_handle != main_window_handler:
                self.switch_window(window_handle)
                self.wait(bpl.ya_locator)
                assert self.get_current_url() == urls.ya_page
                self.switch_window(main_window_handler)





