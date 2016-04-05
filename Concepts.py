class Concepts:
    def __init__(self):
        self.conceptData = self.read_concepts()

    def read_concepts(self):
        return {'indian', 'thai', 'sushi', 'caribbean', 'italian', 'west indian', 'pub', 'east asian',
         'bbq', 'chinese', 'portuguese', 'spanish', 'french', 'east european'}


    def get_matches(self, word):
        lowercase_word = word.lower()
        if lowercase_word in self.conceptData:
            return lowercase_word

