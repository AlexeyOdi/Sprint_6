from pages.main_page import MainPage
import pytest
import allure

@pytest.mark.usefixtures("get_driver_class")
class TestQuestions:

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
    @allure.title('Проверка правильности ответов на вопросы')
    def test_check_answer(self, question, answer, answer_text):
        test_main = MainPage(self.driver)
        test_main.scroll_to_down()
        test_main.click_question(question)
        expected_value = test_main.get_text_to_assert(answer_text)
        actual_value = test_main.get_answer_text(answer)
        test_main.assert_answers(expected_value, actual_value)