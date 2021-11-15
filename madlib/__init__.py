from madlib.grammar import Grammar
from madlib.sentence.sentence_template import SentenceTemplate
from madlib.sentence.sentence_template_collection import SentenceTemplateCollection


def get_sentence():
    collection = SentenceTemplateCollection()
    template = collection.get_random_template()
    s = template.get_sentence()
    return Grammar(s).fix_grammar()
