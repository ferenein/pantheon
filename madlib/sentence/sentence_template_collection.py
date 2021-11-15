from madlib.sentence.sentence_template import SentenceTemplate
import random


class SentenceTemplateCollection:
    def __init__(self):
        self._templates = [
            SentenceTemplate('It was a {adjective} day. I went downstairs to see if I could {verb} dinner. '
                             'I asked, "Does the stew need fresh {noun}?"'),
            SentenceTemplate('Can I have these {adjective} {noun}?')
        ]

    def add_template(self, template_string: str) -> None:
        self._templates.append(SentenceTemplate(template_string))

    def get_template(self, index: int = 0) -> SentenceTemplate:
        template = self._templates[index]
        return template

    def get_random_template(self) -> SentenceTemplate:
        random_index = random.randint(0, len(self._templates) - 1)
        return self.get_template(random_index)
