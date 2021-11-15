from src.word import Category
from src.word.word_interface import WordInterface


DEFAULT_WORDS = {
    Category.NOUN: 'onions',
    Category.VERB: 'cook',
    Category.ADJECTIVE: 'beautiful',
}


class WordMock(WordInterface):
    def get_word(self, word_category: str) -> str:
        return DEFAULT_WORDS[word_category]
