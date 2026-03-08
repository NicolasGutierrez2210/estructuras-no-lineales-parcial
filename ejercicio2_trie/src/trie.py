from typing import Dict, Generator


class TrieNode:
    """
    Nodo del Trie.
    """

    def __init__(self) -> None:
        self.hijos: Dict[str, "TrieNode"] = {}
        self.es_palabra: bool = False


class Trie:
    """
    Implementacion de un Trie para autocompletado de palabras.
    """

    def __init__(self) -> None:
        self.raiz = TrieNode()

    def insertar(self, palabra: str) -> None:
        """
        Inserta una palabra en el Trie.

        Args:
            palabra: palabra que se quiere insertar.
        """

        nodo = self.raiz

        for char in palabra:

            if char not in nodo.hijos:
                nodo.hijos[char] = TrieNode()

            nodo = nodo.hijos[char]

        nodo.es_palabra = True

    def sugerir(self, prefijo: str) -> Generator[str, None, None]:
        """
        Sugiere palabras que comienzan con un prefijo.

        Args:
            prefijo: prefijo de busqueda.

        Yields:
            palabras que comienzan con el prefijo.
        """

        nodo = self.raiz

        for char in prefijo:

            if char not in nodo.hijos:
                return

            nodo = nodo.hijos[char]

        yield from self._dfs(nodo, prefijo)

    def _dfs(self, nodo: TrieNode, prefijo: str) -> Generator[str, None, None]:

        if nodo.es_palabra:
            yield prefijo

        for char, hijo in nodo.hijos.items():
            yield from self._dfs(hijo, prefijo + char)
