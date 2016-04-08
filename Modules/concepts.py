from Modules.trie import Trie


class Concepts:
    def __init__(self, sample_set=True):
        self.conceptData = Trie()

        if sample_set:
            dataset = self.default_dataset()
        else:
            dataset = self.large_dataset()

        self.read_concepts(dataset)

    def large_dataset(self):
        """
        Read the supplied word data file and use the data in the search trie
        :return: list of words
        """

        text_file = open("big_word_list.dat", "r")
        words = text_file.read().split('\n')

        text_file.close()
        return words

    def default_dataset(self):
        word_list = ('indian', 'thai', 'sushi', 'caribbean', 'italian', 'west indian', 'pub', 'east asian',
                     'bbq', 'chinese', 'portuguese', 'spanish', 'french', 'east european', 'japanese sushi shop')
        return word_list

    def read_concepts(self, dataset):
        """
        Create conceptData trie from the default data set, or with the commented out word file.
        """

        for word in dataset:
            self.conceptData[word] = True

    def first_letter_match(self, string_to_find):
        """
        Search for the first letter of the supplied string in the trie
        :param string_to_find:
        :return: True if the first letter exists
        """
        if not string_to_find:
            return False

        return self.conceptData.path.get(string_to_find[0]) is not None

    def match(self, string_to_find):
        """
        Search for the supplied string in the trie in it's entirety.
        :param string_to_find:
        :return: True if the string exists
        """

        if not string_to_find:
            return False

        return self.conceptData.get(string_to_find.lower(), False)
