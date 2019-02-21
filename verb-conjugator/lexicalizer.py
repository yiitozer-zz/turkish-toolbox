from grammar.grammar_rule_checker import GrammarRuleChecker


class Lexicalizer:
    def __init__(self, word):
        self.word = word

    def add_suffix(self, suffix):
        grc = GrammarRuleChecker(word=self.word, suffix=suffix, verbose=True)
        grc.run()
        self.word = grc.word + grc.suffix


l2 = Lexicalizer(word='git')
l2.add_suffix(suffix='yor')