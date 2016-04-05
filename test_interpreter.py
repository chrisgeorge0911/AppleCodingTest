from unittest import TestCase

from interpreter import Interpreter


class TestInterpreter(TestCase):
    def test_getMatchesForString(self):

        interpreter = Interpreter()

        self.assertEqual(interpreter.getMatchesForString('I would like some thai food'), {'thai'})
        self.assertEqual(interpreter.getMatchesForString('Where can I find good sushi'), {'sushi'})
        self.assertEqual(interpreter.getMatchesForString('Find me a place that does tapas'), {})
        self.assertEqual(interpreter.getMatchesForString('Which restaurants do East Asian food'), {'east asian'})
        self.assertEqual(interpreter.getMatchesForString('Which restaurants do West Indian food'), {'west indian', 'indian'})
        self.assertEqual(interpreter.getMatchesForString('What is the weather like today'), {})

    def test_getMatchesForString_emptyString(self):

        interpreter = Interpreter()

        self.assertEqual(interpreter.getMatchesForString(''), {})

