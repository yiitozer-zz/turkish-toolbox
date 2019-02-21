#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

VOWELS = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']


def load_config(config_path):
    with open(config_path, 'r',  encoding="utf-8") as f:
        config_data = yaml.load(f)
    return config_data


def is_last_letter_consonant(word):
    if word[-1] in VOWELS:
        return False
    else:
        return True


def is_first_letter_consonant(word):
    if word[0] in VOWELS:
        return False
    else:
        return True


def get_last_vowel(word_in):
    last_vowel = None
    idx_last_vowel = len(word_in) - 1
    for letter in reversed(word_in):
        if letter in VOWELS:
            last_vowel = letter
            break
        idx_last_vowel -= 1
    return last_vowel, idx_last_vowel


def get_number_of_syllables(word):
    num_syllables = 0
    for letter in word:
        if letter in VOWELS:
            num_syllables += 1
    return num_syllables