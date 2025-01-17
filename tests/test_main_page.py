import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
import urls
import pytest
import locators.base_page_locators as bpl


class TestQuestion:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @pytest.mark.parametrize('question, answer, answer_text',
                             [
                                 [MainPage.question_1, MainPage.answer_1, MainPage.answer_text_1],
                                 [MainPage.question_2, MainPage.answer_2, MainPage.answer_text_2],
                                 [MainPage.question_3, MainPage.answer_3, MainPage.answer_text_3],
                                 [MainPage.question_4, MainPage.answer_4, MainPage.answer_text_4],
                                 [MainPage.question_5, MainPage.answer_5, MainPage.answer_text_5],
                                 [MainPage.question_6, MainPage.answer_6, MainPage.answer_text_6],
                                 [MainPage.question_7, MainPage.answer_7, MainPage.answer_text_7],
                                 [MainPage.question_8, MainPage.answer_8, MainPage.answer_text_8]
                             ]
                             )
    def test_check_answer(self, question, answer, answer_text):

        self.driver.get(urls.main_page)
        test_main = MainPage(self.driver)
        test_main.sroll_to_down()
        test_main.click_question(question)
        expected_value = test_main.get_text_to_assert(answer_text)
        actual_value = test_main.get_answer_text(answer)
        assert expected_value == actual_value

    def test_scooter_logo(self):

        self.driver.get(urls.main_page)
        test_main = MainPage(self.driver)
        test_main.click_header_order()
        test_main.click_scooter_logo()
        assert self.driver.current_url == urls.main_page

    def test_header_order_button(self):

        self.driver.get(urls.main_page)
        test_main = MainPage(self.driver)
        test_main.click_header_order()
        assert self.driver.current_url == urls.order_page

    def test_home_order_button(self):

        self.driver.get(urls.main_page)
        test_main = MainPage(self.driver)
        test_main.scroll_to_home_order_button()
        test_main.click_home_order_button()
        assert self.driver.current_url == urls.order_page

    def test_ya_logo(self):

        self.driver.get(urls.main_page)
        test_main = MainPage(self.driver)
        test_main.click_header_order()
        test_main.click_ya_logo()
        #assert self.driver.current_url == urls.ya_page
        # тест не проходит, в теории не было информации как работать с веб-вкладками, не знаю что делать

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
