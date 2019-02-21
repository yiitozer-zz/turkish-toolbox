import utils
from grammar.grammar_rule import GrammarRule


class ConsonantRule(GrammarRule):
    def __init__(self, config_path="grammar/rule/config/cfg_consonant_rule.yaml", word=None, suffix=None):
        GrammarRule.__init__(self, config_path=config_path, word=word, suffix=suffix)
        self.rules_applied = []

    def run(self):
        if self.is_consonant_softening_applicable():
            self.apply_consonant_softening()
        if self.is_consonant_harmony_applicable():
            self.apply_consonant_harmony()
        if self.is_epenthesis_applicable():
            self.apply_epenthesis()
        if self.is_unlu_turemesi_applicable():
            self.apply_unlu_turemesi()

    def is_consonant_softening_applicable(self):
        word_last_letter = self.word[-1]
        suffix_first_letter = self.suffix[0]
        if word_last_letter in self.config['rules']['softening_rule_lookup'].keys()\
                and suffix_first_letter in self.config['alphabet']['vowels']:
            return True
        else:
            return False

    def apply_consonant_softening(self):
        rule_applied_text = 'Consonant softening applied. ' + self.word + '--->'
        self.word = self.word[:-1] + self.config['rules']['softening_rule_lookup'][self.word[-1]]
        rule_applied_text += self.word
        self.rules_applied.append(rule_applied_text)

    def is_consonant_harmony_applicable(self):
        # ünsüz benzesmesi
        word_last_letter = self.word[-1]
        suffix_first_letter = self.suffix[0]
        if word_last_letter in self.config['alphabet']['hard_consonants'] and suffix_first_letter in \
                self.config['rules']['consonant_harmony_lookup'].keys():
            return True
        else:
            return False

    def apply_consonant_harmony(self):
        rule_applied_text = 'Consonant harmony applied. ' + self.suffix + '--->'
        self.suffix = self.config['rules']['consonant_harmony_lookup'][self.suffix[0]] + self.suffix[1:]
        rule_applied_text += self.suffix
        self.rules_applied.append(rule_applied_text)

    def is_unlu_turemesi_applicable(self):
        if utils.is_last_letter_consonant(self.word) and utils.is_first_letter_consonant(self.suffix):
            return True

    def apply_unlu_turemesi(self):
        rule_applied_text = 'Unlu turemesi applied. ' + self.word + '---> '
        tureyen_unlu = self.config['rules']['vowel_harmony1'][self.last_vowel]
        # The vowel which appears may need to soften a
        if self.is_consonant_softening_applicable():
            self.apply_consonant_softening()
            self.word=self.get_word()
        self.word += tureyen_unlu
        rule_applied_text += self.word
        self.rules_applied.append(rule_applied_text)

    def is_epenthesis_applicable(self):
        pass

    def apply_epenthesis(self):
        pass