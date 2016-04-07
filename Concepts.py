from trie import Trie


class Concepts:
    def __init__(self):
        self.conceptData = Trie()

        self.read_concepts()

    def read_word_file(self):
        text_file = open("word.dat", "r")
        lines = text_file.read().split('\n')

        text_file.close()
        return lines

    def read_concepts(self):
        word_list = ('indian', 'thai', 'sushi', 'caribbean', 'italian', 'west indian', 'pub', 'east asian',
          'bbq', 'chinese', 'portuguese', 'spanish', 'french', 'east european')

        # word_list = self.read_word_file()

        for word in word_list:
            self.conceptData[word] = True

    def first_letter_match(self, string_to_find):
        if not string_to_find:
            return False

        return self.conceptData.path.get(string_to_find[0]) is not None

    def match(self, string_to_find):
        if not string_to_find:
            return False

        return self.conceptData.get(string_to_find.lower(), False)
