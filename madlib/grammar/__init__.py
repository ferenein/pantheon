class Grammar:
    """
    Outside the scope of this project. It probably deserves a microservice on its own.
    """

    def __init__(self, sentence: str = None):
        self._sentence = sentence

    def fix_grammar(self, sentence: str = None) -> str:
        if sentence:
            self._sentence = sentence
        if not self._sentence:
            raise ValueError("No sentence given to fix grammar")

        # TODO: fix grammar for self._sentence
        return self._sentence
