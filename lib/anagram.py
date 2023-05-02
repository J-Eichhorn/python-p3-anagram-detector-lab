# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])

    def match(self, list):
        word_list = []
        for word in list:
            if sorted([letter for letter in word]) == self.word_letters:
                word_list.append(word)
        return word_list