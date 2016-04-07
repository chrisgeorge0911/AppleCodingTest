from unittest import TestCase

from Modules.concepts import Concepts


class TestConcepts(TestCase):

    test_dataset = {
        'indian' : 'indian',
        'thai': 'thai',
        'sushi':'sushi',
        'caribbean': 'caribbean',
        'italian': 'italian',
        'west indian': 'west indian',
        'pub': 'pub',
        'east asian': 'east asian',
        'bbq': 'bbq',
        'chinese': 'chinese',
        'portuguese': 'portuguese',
        'spanish': 'spanish',
        'french': 'french',
        'east european': 'east european'
    }

    def test_read_concepts(self):
        concepts = Concepts()

        self.assertGreater(concepts.conceptData.nodeCount(), 1)

    def test_first_letter_match(self):
        concepts = Concepts()

        self.assertEqual(concepts.first_letter_match('indian'), True)
        self.assertEqual(concepts.first_letter_match('queen'), False)
        self.assertEqual(concepts.first_letter_match('french'), True)

    def test_match(self):
        concepts = Concepts()

        self.assertEqual(concepts.match('indian'), True)
        self.assertEqual(concepts.match('west indian'), True)

        self.assertEqual(concepts.match('wibble'), False)


