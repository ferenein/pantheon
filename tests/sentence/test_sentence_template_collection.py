import unittest

from src.sentence.sentence_template import SentenceTemplate
from src.sentence.sentence_template_collection import SentenceTemplateCollection
from src.word.word_mock import WordMock


class SentenceTemplateTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.collection = SentenceTemplateCollection()

    def test_add_template(self):
        self.collection.add_template('Can I {verb} these {adjective} {noun}?')
        self.assertEqual(len(self.collection._templates), 3, 'Length of the collection is wrong')

        template = self.collection.get_template(-1)
        template._word_generator = WordMock()

        expected_result = 'Can I cook these beautiful onions?'
        result = template.get_sentence()
        self.assertEqual(expected_result, result)

    def test_get_template(self):
        template = self.collection.get_template()
        expected_result = 'It was a {adjective} day. I went downstairs to see if I could {verb} dinner. ' \
                          'I asked, "Does the stew need fresh {noun}?"'
        self.assertEqual(template._template_string, expected_result)