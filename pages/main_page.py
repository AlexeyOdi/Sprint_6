from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import urls
import locators.base_page_locators as bpl
import allure

class MainPage:

    driver = None

    question_1 = [By.XPATH, '//div[@class="accordion"]/child::div[1]']
    answer_1 = [By.XPATH, '//div[@class="accordion"]/child::div[1]/div[2]']
    answer_text_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    question_2 = [By.XPATH, '//div[@class="accordion"]/child::div[2]']
    answer_2 = [By.XPATH, '//div[@class="accordion"]/child::div[2]/div[2]']
    answer_text_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    question_3 = [By.XPATH, '//div[@class="accordion"]/child::div[3]']
    answer_3 = [By.XPATH, '//div[@class="accordion"]/child::div[3]/div[2]']
    answer_text_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    question_4 = [By.XPATH, '//div[@class="accordion"]/child::div[4]']
    answer_4 = [By.XPATH, '//div[@class="accordion"]/child::div[4]/div[2]']
    answer_text_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    question_5 = [By.XPATH, '//div[@class="accordion"]/child::div[5]']
    answer_5 = [By.XPATH, '//div[@class="accordion"]/child::div[5]/div[2]']
    answer_text_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    question_6 = [By.XPATH, '//div[@class="accordion"]/child::div[6]']
    answer_6 = [By.XPATH, '//div[@class="accordion"]/child::div[6]/div[2]']
    answer_text_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    question_7 = [By.XPATH, '//div[@class="accordion"]/child::div[7]']
    answer_7 = [By.XPATH, '//div[@class="accordion"]/child::div[7]/div[2]']
    answer_text_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    question_8 = [By.XPATH, '//div[@class="accordion"]/child::div[8]']
    answer_8 = [By.XPATH, '//div[@class="accordion"]/child::div[8]/div[2]']
    answer_text_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на вопрос')
    def click_question(self, question):
        self.driver.find_element(*question).click()

    @allure.step('Получаем текст фактического ответа')
    def get_answer_text(self, answer):
        return self.driver.find_element(*answer).text

    @allure.step('Прокручиваем страницу до самого низа')
    def sroll_to_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Прокручиваем страницу до кнопки "заказать" в середине страницы')
    def scroll_to_home_order_button(self):
        element = self.driver.find_element(*bpl.home_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)

    @allure.step('Получаем текст ожидаемого ответа')
    def get_text_to_assert(self, answer_text):
        return answer_text

    @allure.step('Кликаем на кнопку "заказать" в шапке страницы')
    def click_header_order(self):
        self.driver.find_element(*bpl.header_order_button).click()

    @allure.step('Кликаем лого самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*bpl.scooter_logo).click()

    @allure.step('Кликаем лого Яндекс')
    def click_ya_logo(self):
        self.driver.find_element(*bpl.ya_logo).click()

    @allure.step('Кликаем кнопку "заказать" в середине страницы')
    def click_home_order_button(self):
        self.driver.find_element(*bpl.home_order_button).click()

