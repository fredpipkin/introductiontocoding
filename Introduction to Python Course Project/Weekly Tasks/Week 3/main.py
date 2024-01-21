from pigLatin import *

sentence_to_translate = input('Please enter the phrase that you would like translated to pig latin: ')

translation = PigLatinHelper.translate(sentence_to_translate)

print('Translation is: ' + translation)
