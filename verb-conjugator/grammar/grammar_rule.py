from utils import load_config, get_last_vowel, get_number_of_syllables


class GrammarRule:
    def __init__(self, config_path=None, word=None, suffix=None):
        self.word = word
        self.suffix = suffix
        self.config = load_config(config_path)
        self.rules_applied = []
        self.last_vowel, self.idx_last_vowel = get_last_vowel(word)
        self.num_syllables = get_number_of_syllables(self.word)

    def get_word(self):
        return self.word

    def get_suffix(self):
        return self.suffix

    def get_rules_applied(self):
        return self.rules_applied

    def print_applied_rules(self):
        for rule_applied in self.rules_applied:
            print(rule_applied)
