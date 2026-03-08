from typing import Any, List, Tuple


class HashTable:
    def __init__(self, size: int = 10) -> None:
        self.size: int = size
        self.table: List[List[Tuple[Any, Any]]] = [[] for _ in range(size)]

    def _hash(self, key: Any) -> int:
        return hash(key) % self.size

    def insert(self, key: Any, value: Any) -> None:
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))

    def get(self, key: Any) -> Any:
        index = self._hash(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        return None

    def delete(self, key: Any) -> bool:
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True

        return False

    # Método mágico requerido en el ejercicio
    def __setitem__(self, key: Any, value: Any) -> None:
        self.insert(key, value)

    # Bonus: permite acceder con tabla[key]
    def __getitem__(self, key: Any) -> Any:
        return self.get(key)
