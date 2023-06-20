import itertools

class AnagramChecker:
    def __init__(self):
        self.dictionary = []
        self.load_dictionary()


    def load_dictionary(self):
        with open('dictionary.txt', 'r') as f:
            for line in f:
                line = line.strip()
                self.dictionary.append(line.lower())

        # print(self.dictionary)

    def is_valid_word(self,word):
        if word in self.dictionary:
            return True
        else:
            return False
        
    def get_anagrams(self,word):
        anagrams=[]
        variations=self.get_variations(word)
        for variation in variations:
            if self.is_valid_word(variation):
                if variation not in anagrams and variation!=word:
                    anagrams.append(variation)
        return anagrams
    

    def get_variations(self,word):
        variations=["".join(word) for word in itertools.permutations(word)]
        # print(variations)
        return variations
