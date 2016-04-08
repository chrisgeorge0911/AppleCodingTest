import unittest

from unittest import TestCase
import time

from datetime import timedelta

from Modules.interpreter import Interpreter


class TestInterpreter(TestCase):

    interpreter = Interpreter(False)

    def test_getMatchesForString(self):
        self.assertEqual(self.interpreter.get_matches_for_string('I would like some thai food'), ['i', 'would', 'like', 'some', 'thai', 'food'])

    def test_getMatchesForString_no_matches(self):

        start_time = time.clock()
        matches = self.interpreter.get_matches_for_string('abcdd efggh ijklm nopq rstuvw xxyz')
        end_time = time.clock()

        self.assertEqual(matches, [])

        # check that the time taken to return zero matches (should be longest path) is less than 1ms
        self.assertLess(end_time - start_time, 0.001)


if __name__ == "__main__":
    unittest.main()
