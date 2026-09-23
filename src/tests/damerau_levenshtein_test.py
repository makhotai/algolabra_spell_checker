import unittest
import hypothesis.strategies as st
from hypothesis import given, settings

from services.damerau_levenshtein import distance_full
from services.osa import distance


class TestDamerauLevenshtein(unittest.TestCase):
    def test_similar_words(self):
        self.assertEqual(distance_full("apple", "apple"), 0)
        self.assertNotEqual(distance_full("appl", "apple"), 0)

    def test_insertion_is_1(self):
        self.assertEqual(distance_full("aple", "apple"), 1)

    def test_deletion_is_1(self):
        self.assertEqual(distance_full("koirra", "koira"), 1)

    def test_substitution_is_1(self):
        self.assertEqual(distance_full("tavle", "table"), 1)

    def test_transposition_is_1(self):
        self.assertEqual(distance_full("leisi", "liesi"), 1)

    def test_adjacent_transpositions(self):
        self.assertEqual(distance_full("ca", "abc"), 2)

    def test_n_operations_is_n(self):
        self.assertEqual(distance_full("valita", "valittaa"), 2)
        self.assertEqual(distance_full("kulma", "kylmä"), 2)
        self.assertEqual(distance_full("tuuli", "tule"), 2)
    
    def test_full_distance_less_than_osa(self):
        self.assertLessEqual(distance_full("ca", "abc"), distance("ca", "abc"))
        self.assertLessEqual(distance_full("flom", "molf"), distance("flom", "molf"))

    def test_complitely_different(self):
        word1 = "qwert"
        word2 = "zxcvb"
        n = max(len(word1), len(word2))
        self.assertEqual(distance_full(word1, word2), n)

        word2 = "zxcvbnm"
        n = max(len(word1), len(word2))
        self.assertEqual(distance_full(word1, word2), n)

    @given(val=st.text(alphabet= st.characters(codec="utf-8"),
                       min_size=2, max_size=70))
    @settings(max_examples=500)
    def test_distance_for_same_long_words_hypothesis(self, val):
        self.assertEqual(distance_full(val, val), 0)

    @given(val1=st.text(alphabet= st.characters(codec="utf-8"),
                        min_size=3, max_size=40),
           val2=st.text(alphabet= st.characters(codec="utf-8"),
                        min_size=3, max_size=40))
    @settings(max_examples=500)
    def test_distance_for_longer_words_hypothesis(self, val1, val2):
        if val1 != val2:
            self.assertLessEqual(distance_full(val1, val2), distance(val1, val2))
