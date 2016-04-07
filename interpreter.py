import string
import unicodedata

from concepts import Concepts


class Interpreter:

    def get_matches_for_string(self, sentence):

        # convert accented and other special characters to their standard character equivalent
        sentence = unicodedata.normalize('NFKD', sentence).encode('ASCII', 'ignore').decode('UTF-8')

        # remove punctuation marks
        exclude = set(string.punctuation)
        sentence = ''.join(ch for ch in sentence if ch not in exclude)

        concepts = Concepts()

        matched_list = []

        words = sentence.lower().split(' ')

        for i in range(0, len(words)):

            if concepts.first_letter_match(words[i]):

                for j in range(i, len(words)):

                    # print("word: {}".format(words[i]))
                    joined_word = ' '.join(words[i:j+1])

                    # print("joined word: {}".format(joined_word))

                    if concepts.match(joined_word):
                        if joined_word not in matched_list:
                            matched_list.append(joined_word)

        return matched_list

