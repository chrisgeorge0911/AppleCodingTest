from unittest import TestCase

from interpreter import Interpreter


class TestInterpreter(TestCase):
    def test_getMatchesForString(self):

        interpreter = Interpreter()

        self.assertEqual(interpreter.get_matches_for_string('I would like some thai food'), ['thai'])
        self.assertEqual(interpreter.get_matches_for_string('Where can I find good sushi'), ['sushi'])
        self.assertEqual(interpreter.get_matches_for_string('Find me a place that does tapas'), [])
        self.assertEqual(interpreter.get_matches_for_string('Which restaurants do East Asian food'), ['east asian'])
        self.assertEqual(interpreter.get_matches_for_string('Which restaurants do West Indian food'), ['west indian', 'indian'])
        self.assertEqual(interpreter.get_matches_for_string('What is the weather like today'), [])

    def test_getMatchesForString_word_positioning(self):
        interpreter = Interpreter()

        self.assertEqual(interpreter.get_matches_for_string('thai food is what I would like'), ['thai'])

    def test_getMatchesForString_whitespace(self):
        interpreter = Interpreter()

        self.assertEqual(interpreter.get_matches_for_string('I would like some   thai food'), ['thai'])

    def test_getMatchesForString_duplicates(self):
        interpreter = Interpreter()

        self.assertEqual(interpreter.get_matches_for_string('sushi sushi sushi'), ['sushi'])
        self.assertEqual(interpreter.get_matches_for_string('thai food is the thai food I would like'), ['thai'])
        self.assertEqual(interpreter.get_matches_for_string('thai thai sushi thai sushi sushi'), ['thai', 'sushi'])
        self.assertEqual(interpreter.get_matches_for_string('east asian west indian indian indian'), ['east asian', 'west indian', 'indian'])
        self.assertEqual(interpreter.get_matches_for_string('east asian west indian indian indian east'), ['east asian', 'west indian', 'indian'])

    def test_getMatchesForString_special_characters(self):
        interpreter = Interpreter()

        self.assertEqual(interpreter.get_matches_for_string('èast asian'), ['east asian'])

    def test_getMatchesForString_punctuation(self):
        interpreter = Interpreter()

        self.assertEqual(interpreter.get_matches_for_string('lots of italian, more chinese'), ['italian', 'chinese'])

    def test_getMatchesForString_max_words(self):
        interpreter = Interpreter()

        self.assertEqual(interpreter.get_matches_for_string('let\'s go down the pub and have a bbq italian meal whilst in the caribbean speaking spanish french and chinese'), ['pub','bbq','italian','caribbean','spanish','french','chinese'])

    def test_getMatchesForString_emptyString(self):
        interpreter = Interpreter()

        self.assertEqual(interpreter.get_matches_for_string(''), [])

