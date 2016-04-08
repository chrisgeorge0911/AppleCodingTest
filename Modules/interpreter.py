import string
import unicodedata

from Modules.concepts import Concepts


class Interpreter:

    def __init__(self):
        # read the concept data
        self.concepts = Concepts()

    def get_matches_for_string(self, sentence):
        """
        Search for concepts in the supplied sentence
        :param sentence:
        :return: List of concepts that exist in the sentence
        """

        sanitised_sentence = self.sanitise_string(sentence)

        # make list of words, lowercasing the text during this process
        words = sanitised_sentence.lower().split(' ')

        matched_list = self.find_concepts_in_string(words)

        return matched_list

    def sanitise_string(self, sentence):
        # convert accented and other special characters to their standard character equivalent
        sentence = unicodedata.normalize('NFKD', sentence).encode('ASCII', 'ignore').decode('UTF-8')

        # remove punctuation marks
        exclude = set(string.punctuation)
        sentence = ''.join(ch for ch in sentence if ch not in exclude)

        return sentence

    def find_concepts_in_string(self, words):
        """
        Iterate over every word, and for each word check if there is the possibility that it exists in the data set.
        If so, continue iterating over the list of words to find all possible matches.
        :param words:
        :return:
        """

        matched_list = []
        for i in range(0, len(words)):

            if self.concepts.first_letter_match(words[i]):

                for j in range(i, len(words)):

                    # print("word: {}".format(words[i]))
                    joined_word = ' '.join(words[i:j + 1])

                    # print("joined word: {}".format(joined_word))

                    if self.concepts.match(joined_word):
                        if joined_word not in matched_list:
                            matched_list.append(joined_word)

        return matched_list
