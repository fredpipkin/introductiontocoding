from pigLatin import *

def test_translation_starting_with_single_consonant():
    assert PigLatinHelper.translate("pig") == "igpay"

def test_translation_starting_with_multiple_consonants():
    assert PigLatinHelper.translate("friends") == "iendsfray"

def test_translation_starting_with_vowel():
    assert PigLatinHelper.translate("eat") == "eathay"

def test_translation_no_vowels():
    assert PigLatinHelper.translate("fly") == "flyhay"

def test_translation_of_a_sentence():
    assert PigLatinHelper.translate("this is a test sentence") == "isthay ishay ahay esttay entencesay"