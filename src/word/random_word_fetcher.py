from src.shared import request
from src.word.word_interface import WordInterface
from src.word.word_mock import DEFAULT_WORDS


class RandomWordFetcher(WordInterface):
    BASE_URL = 'https://reminiscent-steady-albertosaurus.glitch.me/'

    def get_word(self, word_category: str) -> str:
        url = self.BASE_URL + word_category
        try:
            word = request.get(url).text
            return word.strip('\"')
        except Exception as ex:
            return DEFAULT_WORDS[word_category]