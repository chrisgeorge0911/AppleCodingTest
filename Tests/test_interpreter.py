import unittest
from unittest import TestCase

from Modules.interpreter import Interpreter


class TestInterpreter(TestCase):

    interpreter = Interpreter()

    def test_getMatchesForString(self):

        self.assertEqual(self.interpreter.get_matches_for_string('I would like some thai food'), ['thai'])
        self.assertEqual(self.interpreter.get_matches_for_string('Where can I find good sushi'), ['sushi'])
        self.assertEqual(self.interpreter.get_matches_for_string('Find me a place that does tapas'), [])
        self.assertEqual(self.interpreter.get_matches_for_string('Which restaurants do East Asian food'), ['east asian'])
        self.assertEqual(self.interpreter.get_matches_for_string('Which restaurants do West Indian food'), ['west indian', 'indian'])
        self.assertEqual(self.interpreter.get_matches_for_string('What is the weather like today'), [])

    def test_getMatchesForString_multi_word(self):
        self.assertEqual(self.interpreter.get_matches_for_string('I went to a japanese sushi shop to buy sushi'), ['japanese sushi shop', 'sushi'])

    def test_getMatchesForString_word_positioning(self):

        self.assertEqual(self.interpreter.get_matches_for_string('thai food is what I would like'), ['thai'])

    def test_getMatchesForString_whitespace(self):

        self.assertEqual(self.interpreter.get_matches_for_string('I would   like some   thai   food'), ['thai'])

    def test_getMatchesForString_duplicates(self):

        self.assertEqual(self.interpreter.get_matches_for_string('sushi sushi sushi'), ['sushi'])
        self.assertEqual(self.interpreter.get_matches_for_string('thai food is the thai food I would like'), ['thai'])
        self.assertEqual(self.interpreter.get_matches_for_string('thai thai sushi thai sushi sushi'), ['thai', 'sushi'])
        self.assertEqual(self.interpreter.get_matches_for_string('east asian west indian indian indian'), ['east asian', 'west indian', 'indian'])
        self.assertEqual(self.interpreter.get_matches_for_string('east asian west indian indian indian east'), ['east asian', 'west indian', 'indian'])

    def test_getMatchesForString_special_characters(self):

        self.assertEqual(self.interpreter.get_matches_for_string('èast asian'), ['east asian'])

    def test_getMatchesForString_punctuation(self):

        self.assertEqual(self.interpreter.get_matches_for_string('lots of italian, more chinese'), ['italian', 'chinese'])

    def test_getMatchesForString_max_words(self):

        self.assertEqual(self.interpreter.get_matches_for_string('let\'s go down the pub and have a bbq italian meal whilst in the caribbean speaking spanish french and chinese'), ['pub','bbq','italian','caribbean','spanish','french','chinese'])

    def test_getMatchesForString_emptyString(self):

        self.assertEqual(self.interpreter.get_matches_for_string(''), [])
        self.assertEqual(self.interpreter.get_matches_for_string(None), [])


if __name__ == "__main__":
    unittest.main()
