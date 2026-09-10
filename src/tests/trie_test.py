import unittest
from services.trie import TrieNode, Trie

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
    
    def test_trie_word_count_correct(self):
        trie_count = Trie()
        n = 4
        self.assertEqual(trie_count._size, 0)
        self.assertNotEqual(trie_count._size, n)
        

        wordlist = ["one", "two", "three", "four", "five", "six"]
        for i in range(n):
            trie_count.insert(wordlist[i])
        self.assertEqual(trie_count._size, n)
        
    def test_cannot_insert_empty_string(self):
        empty_trie = Trie()
        empty_trie.insert("")
        self.assertEqual(empty_trie._size, 0)