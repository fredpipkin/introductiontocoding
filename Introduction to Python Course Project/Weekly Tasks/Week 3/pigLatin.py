class PigLatinHelper:
    @staticmethod
    def translate(sentence: str) -> str:
        words = sentence.split()
        translation = []

        for word in words:
            translation.append(PigLatinHelper.translate_word(word))

        return ' '.join(translation)
        
    @staticmethod
    def translate_word(word: str) -> str:
        indexofvowel = PigLatinHelper.find_index_of_first_vowel(word)

        if indexofvowel <= 0:
            result = word + 'hay'
        else:
            result = word[indexofvowel:] + word[:indexofvowel] + 'ay'

        return result

    @staticmethod
    def find_index_of_first_vowel(word: str) -> int:
        vowels = 'aeiou'

        for index, char in enumerate(word):
            if char in 'AaeEiIoOuU':
                return index
            
        return -1


    
