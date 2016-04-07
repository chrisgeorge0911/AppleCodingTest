from concepts import Concepts


class Interpreter:

    def get_matches_for_string(self, sentence):

        concepts = Concepts()

        matched_list = []

        words = sentence.lower().split(' ')

        for i in range(0,len(words)):

            if concepts.first_letter_match(words[i]):

                for j in range(i, len(words)):

                    # print("word: {}".format(words[i]))
                    joined_word = ' '.join(words[i:j+1])

                    # print("joined word: {}".format(joined_word))

                    if concepts.match(joined_word):
                        matched_list.append(joined_word)

        return matched_list

