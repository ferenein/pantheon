from madlib.word import Category
from madlib.word.random_word_fetcher import RandomWordFetcher
from madlib.word.word_interface import WordInterface


class SentenceTemplate:
    def __init__(self, template_string: str, word_generator: WordInterface = None):
        self._template_string = template_string
        self._counts = dict()
        self._word_generator = word_generator or RandomWordFetcher()

    def get_sentence(self) -> str:
        keyword_args = self.get_words()
        sentence = self._template_string.format(**keyword_args)
        return sentence

    def get_words(self) -> dict:
        self._prepare()

        # TODO: send parallel requests
        words = {}
        words.update(self._get_word(Category.NOUN))
        words.update(self._get_word(Category.VERB))
        words.update(self._get_word(Category.ADJECTIVE))
        return words

    def _get_word(self, word_category: str) -> dict:
        return {word_category: self._word_generator.get_word(word_category) for i in range(self._counts[word_category])}

    def _prepare(self) -> None:
        self._count_word_categories()
        # TODO: Support multiple adjectives, verbs, and/or nouns.
        #  if a sentence template has multiple (let's say) adjectives, the second and third ones
        #  should be replaced with a different variable name such as adjective2 and adjective3.

    def _count_word_categories(self) -> None:
        """
        Count the number of adj, verb, nouns needed for a template.
        """
        self._count(Category.VERB)
        self._count(Category.NOUN)
        self._count(Category.ADJECTIVE)

    def _count(self, word_category: str) -> None:
        """
        Lazy implementation to count a word category
        :return: None
        """
        if word_category not in self._counts:
            self._counts[word_category] = self._template_string.count("{" + word_category + "}")
