from typing import Protocol


class WordInterface(Protocol):
    def get_word(self, word_type):
        raise NotImplementedError("This function must be implemented")
