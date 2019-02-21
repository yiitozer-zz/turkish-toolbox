from grammar.rule.consonant_rule import ConsonantRule
from grammar.rule.vowel_rule import VowelRule


class GrammarRuleChecker:
    def __init__(self, word, suffix, verbose=False):
        self.word = word
        self.suffix = suffix
        self.verbose = verbose
        self.applied_rules = []

    def run(self):
        if self.verbose:
            print('##########################')
            print('Word input: ', self.word + '.', 'Suffix: ', self.suffix)
            print('##########################')

        self.apply_consonant_rules()
        self.apply_vowel_rules()
        if self.verbose:
            self.print_rules_applied()
            print('##########################')
            print('Output:', self.word + self.suffix)

    def apply_consonant_rules(self):
        # 1. Yumusama
        cr = ConsonantRule(word=self.word, suffix=self.suffix)
        cr.run()

        self.word = cr.get_word()
        self.suffix = cr.get_suffix()
        self.applied_rules += cr.get_rules_applied()

        # 3. Kaynasma

    def apply_vowel_rules(self):
        # 1. Big Vowel Harmony
        vr = VowelRule(word=self.word, suffix=self.suffix)
        vr.run()
        self.word = vr.get_word()
        self.suffix = vr.get_suffix()
        self.applied_rules += vr.get_rules_applied()

    def print_rules_applied(self):
        num_rule = 1
        for applied_rule in self.applied_rules:
            print(str(num_rule) + '.' + applied_rule)
            num_rule += 1

'''
grc = GrammarRuleChecker('kayıp', 'a', verbose=True)
grc.run()

grc2 = GrammarRuleChecker('beyin', 'e', verbose=True)
grc2.run()

grc3 = GrammarRuleChecker('oyna', 'yor', verbose=True)
grc3.run()

grc4 = GrammarRuleChecker('kalp', 'e', verbose=True)
grc4.run()

grc5 = GrammarRuleChecker('ataç', 'a', verbose=True)
grc5.run()

grc6 = GrammarRuleChecker('kaltak', 'ı', verbose=True)
grc6.run()
'''