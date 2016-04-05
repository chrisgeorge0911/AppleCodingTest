from unittest import TestCase

from concepts import Concepts


class TestConcepts(TestCase):

    def test_get_matches_all_dataset_values(self):
        concepts = Concepts()

        # check that the match works for all discrete values in the concepts data set
        for concept in concepts.conceptData:
            self.assertEqual(concepts.get_matches(concept), concept.lower())

    def test_get_matches_all_dataset_values_uppercase(self):
        concepts = Concepts()

        # check that the match is case insensitive
        for concept in concepts.conceptData:
            self.assertEqual(concepts.get_matches(concept.upper()), concept.lower())


