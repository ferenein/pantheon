from src.grammar import Grammar
from src.sentence.sentence_template import SentenceTemplate
from src.sentence.sentence_template_collection import SentenceTemplateCollection


def get_sentence():
    collection = SentenceTemplateCollection()
    template = collection.get_random_template()
    s = template.get_sentence()
    return Grammar(s).fix_grammar()
