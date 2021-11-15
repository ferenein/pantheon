from madlib.shared import request
from madlib.word.word_interface import WordInterface
from madlib.word.word_mock import DEFAULT_WORDS


class RandomWordFetcher(WordInterface):
    BASE_URL = 'https://reminiscent-steady-albertosaurus.glitch.me/'

    def get_word(self, word_category: str) -> str:
        url = self.BASE_URL + word_category
        try:
            word = request.get(url).text
            return word.strip('\"')
        except Exception as ex:
            return DEFAULT_WORDS[word_category]