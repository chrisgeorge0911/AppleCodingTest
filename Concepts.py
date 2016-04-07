from trie import Trie


class Concepts:
    def __init__(self):
        self.conceptData = Trie()

        self.read_concepts()

    def read_concepts(self):
        word_list = ('indian', 'thai', 'sushi', 'caribbean', 'italian', 'west indian', 'pub', 'east asian',
         'bbq', 'chinese', 'portuguese', 'spanish', 'french', 'east european')

        for word in word_list:
            self.conceptData[word] = True

    def first_letter_match(self, string_to_find):
        return self.conceptData.path.get(string_to_find[0]) is not None

    def match(self, string_to_find):
        return self.conceptData.get(string_to_find.lower(), False)
