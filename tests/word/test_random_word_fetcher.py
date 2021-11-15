import httpretty
import unittest

from madlib.word import Category
from madlib.word.random_word_fetcher import RandomWordFetcher
from madlib.word.word_mock import DEFAULT_WORDS


class RandomWordFetcherTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.word_fetcher = RandomWordFetcher()

    @httpretty.activate
    def test_get_noun(self) -> None:
        httpretty.register_uri(httpretty.GET, RandomWordFetcher.BASE_URL + Category.NOUN,
                               body='"food"')
        result = self.word_fetcher.get_word(Category.NOUN)
        self.assertEqual(result, 'food')

    @httpretty.activate
    def test_api_fail_returns_default_word(self) -> None:
        httpretty.register_uri(httpretty.GET, RandomWordFetcher.BASE_URL + Category.NOUN,
                               status=400)
        result = self.word_fetcher.get_word(Category.NOUN)
        self.assertEqual(result, DEFAULT_WORDS.get(Category.NOUN))