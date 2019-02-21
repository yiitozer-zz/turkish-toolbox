import utils
from grammar.grammar_rule import GrammarRule
from grammar.rule.consonant_rule import ConsonantRule

class VowelRule(GrammarRule):
    def __init__(self, config_path='grammar/rule/config/cfg_vowel_rule.yaml', word=None, suffix=None):
        GrammarRule.__init__(self, config_path=config_path, word=word, suffix=suffix)
        self.rules_applied = []

    def run(self):
        if self.is_haplology_applicable():
            self.apply_haplology()
        if self.is_vowel_fracture_applicable():
            self.apply_vowel_fracture()

    def big_vowel_harmony(self):
        # Büyük ünlü uyumu
        pass

    def small_vowel_harmony(self):
        # Kücük ünlü uyumu
        pass

    def is_epenthesis_applicable(self):
        # Ünlü daralmasi

        pass

    def apply_epenthesis(self):
        pass

    def is_vowel_fracture_applicable(self):
        if self.word[-1] in self.config['rules']['vowel_fracture_lookup'] and (self.suffix == 'yor' or self.suffix == 'iyor'):
            return True
        else:
            return False

    def apply_vowel_fracture(self):
        rule_applied_text = 'Vowel fracture applied. ' + self.word + '--->'
        if self.num_syllables == 1:
            self.word = self.word[:-1] + self.config['rules']['vowel_harmony1'][self.word[-1]]
        else:
            penultimate_vowel, _ = utils.get_last_vowel(self.word[:-1])
            self.word = self.word[:-1] + self.config['rules']['vowel_harmony1'][penultimate_vowel]

        rule_applied_text += self.word
        self.rules_applied.append(rule_applied_text)

    def is_haplology_applicable(self):
        # Ünlü düsmesi
        # TODO: There are exceptions
        if self.last_vowel in self.config['alphabet']['close_vowels'] and self.num_syllables == 2 and \
                        self.suffix[0] in self.config['alphabet']['vowels']:
            return True
        else:
            return False

    def apply_haplology(self):
        rule_applied_text = 'Haplology applied. ' + self.word + '---> '
        self.word = self.word[0:self.idx_last_vowel] + self.word[self.idx_last_vowel+1:]
        rule_applied_text += self.word
        self.rules_applied.append(rule_applied_text)