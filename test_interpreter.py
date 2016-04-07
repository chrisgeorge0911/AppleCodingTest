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


    def test_getMatchesForString_emptyString(self):

        interpreter = Interpreter()

        self.assertEqual(interpreter.get_matches_for_string(''), [])

