import unittest
from src.hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self) -> None:
        self.table = HashTable()

    def test_insert_and_get(self) -> None:
        self.table.insert(1, "Juan")
        self.assertEqual(self.table.get(1), "Juan")

    def test_update(self) -> None:
        self.table.insert(1, "Juan")
        self.table.insert(1, "Carlos")
        self.assertEqual(self.table.get(1), "Carlos")

    def test_delete(self) -> None:
        self.table.insert(2, "Maria")
        self.table.delete(2)
        self.assertIsNone(self.table.get(2))

    def test_magic_setitem(self) -> None:
        self.table[3] = "Ana"
        self.assertEqual(self.table.get(3), "Ana")

    def test_magic_getitem(self) -> None:
        self.table[4] = "Pedro"
        self.assertEqual(self.table[4], "Pedro")


if __name__ == "__main__":
    unittest.main()
