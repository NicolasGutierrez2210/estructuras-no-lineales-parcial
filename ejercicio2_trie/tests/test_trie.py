import unittest
from src.trie import Trie


class TestTrie(unittest.TestCase):

    def test_sugerencias(self):

        trie = Trie()

        trie.insertar("python")
        trie.insertar("pycharm")
        trie.insertar("pyramid")

        resultados = list(trie.sugerir("py"))

        self.assertIn("python", resultados)
        self.assertIn("pycharm", resultados)


if __name__ == "__main__":
    unittest.main()
