import hypothesis.strategies as st
from hypothesis import given, settings
import unittest
from services.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("apple")
        self.trie.insert("raven")
        self.trie.insert("yö")
        self.trie.insert("kynä")
        self.trie.insert("ångström")

    def test_word_inserted_and_contained(self):
        self.assertTrue(self.trie.contains("apple"))
        self.assertTrue(self.trie.contains("raven"))
        self.assertTrue(self.trie.contains("yö"))
        self.assertTrue(self.trie.contains("kynä"))
        self.assertTrue(self.trie.contains("ångström"))

    def test_word_not_inserted_and_contained(self):
        self.assertFalse(self.trie.contains("a"))
        self.assertFalse(self.trie.contains("aaa"))
        self.assertFalse(self.trie.contains("toinen"))

    def test_prefix_of_word_not_itself_a_word(self):
        trie_pref = Trie()
        trie_pref.insert("abcde")
        self.assertFalse(trie_pref.contains("a"))
        self.assertFalse(trie_pref.contains("abcd"))
        self.assertTrue(trie_pref.contains("abcde"))

    def test_longer_word_not_found(self):
        trie_long = Trie()
        trie_long.insert("long")
        self.assertFalse(trie_long.contains("longer"))
        self.assertTrue(trie_long.contains("long"))

    def test_same_prefix_words_stored_correctly(self):
        trie_same = Trie()
        trie_same.insert("cat")
        trie_same.insert("car")
        trie_same.insert("cart")
        self.assertTrue(trie_same.contains("car"))
        self.assertTrue(trie_same.contains("cart"))
        self.assertTrue(trie_same.contains("car"))

    def test_cannot_add_same_word_twice(self):
        trie_double = Trie()
        trie_double.insert("same")
        trie_double.insert("same")
        self.assertEqual(len(trie_double), 1)

    def test_trie_word_count_correct(self):
        trie_count = Trie()
        n = 4
        self.assertEqual(trie_count._size, 0)
        self.assertNotEqual(trie_count._size, n)

        wordlist = ["one", "two", "three", "four", "five", "six"]
        for i in range(n):
            trie_count.insert(wordlist[i])
        self.assertEqual(len(trie_count), n)

    def test_cannot_insert_empty_string(self):
        empty_trie = Trie()
        empty_trie.insert("")
        self.assertEqual(empty_trie._size, 0)

    @given(val=st.text(alphabet= st.characters(codec="utf-8"), min_size=2, max_size=70))
    @settings(max_examples=1000)
    def test_all_possible_str_inserted_hypothesis(self, val):
        all_str = Trie()
        all_str.insert(val)
        self.assertTrue(all_str.contains(val))
