import unittest

from src.sentence.sentence_template import SentenceTemplate
from src.word.word_mock import WordMock, DEFAULT_WORDS


class SentenceTemplateTestCase(unittest.TestCase):
    def setUp(self) -> None:
        template_string = 'It was a {adjective} day. I went downstairs to see if I could {verb} dinner. ' \
                          'I asked, "Does the stew need fresh {noun}?"'
        self.template = SentenceTemplate(template_string, WordMock())

    def test_get_words(self):
        result = self.template.get_words()
        self.assertEqual(result, DEFAULT_WORDS)

    def test_get_sentence(self):
        expected_result = 'It was a beautiful day. I went downstairs to see if I could cook dinner. ' \
                          'I asked, "Does the stew need fresh onions?"'
        result = self.template.get_sentence()
        self.assertEqual(result, expected_result)

    def test_get_words_only_adjective(self):
        template_string = 'It was a {adjective} day.'
        template = SentenceTemplate(template_string, WordMock())

        expected_result = {
            'adjective': 'beautiful'
        }
        result = template.get_words()
        self.assertEqual(result, expected_result)

    def test_get_sentence_only_adjective(self):
        template_string = 'It was a {adjective} day.'
        template = SentenceTemplate(template_string, WordMock())

        expected_result = 'It was a beautiful day.'
        result = template.get_sentence()
        self.assertEqual(result, expected_result)
