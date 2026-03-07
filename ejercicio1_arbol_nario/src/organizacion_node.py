from __future__ import annotations
from typing import Dict, Iterator


class OrganizacionNode:
    """
    Representa un nodo dentro de una estructura organizacional
    modelada como un arbol N-ario.

    Cada nodo puede tener multiples hijos identificados por nombre.
    """

    def __init__(self, nombre: str) -> None:
        """
        Inicializa un nodo de la organizacion.

        Args:
            nombre: nombre del nodo dentro de la organizacion.
        """

        self.nombre: str = nombre
        self.hijos: Dict[str, OrganizacionNode] = {}

    def agregar_hijo(self, nombre: str) -> None:
        """
        Agrega un nuevo hijo al nodo actual.

        Args:
            nombre: nombre del nodo hijo a agregar.

        Raises:
            ValueError: si el hijo ya existe.
        """

        if nombre in self.hijos:
            raise ValueError("El hijo ya existe")

        self.hijos[nombre] = OrganizacionNode(nombre)

    def obtener_hijo(self, nombre: str) -> OrganizacionNode:
        """
        Obtiene un nodo hijo por su nombre.

        Args:
            nombre: nombre del nodo hijo.

        Returns:
            OrganizacionNode: nodo hijo encontrado.

        Raises:
            KeyError: si el hijo no existe.
        """

        if nombre not in self.hijos:
            raise KeyError("Hijo no encontrado")

        return self.hijos[nombre]

    def __iter__(self) -> Iterator["OrganizacionNode"]:
        """
        Permite recorrer el arbol utilizando un bucle for.

        Yields:
            OrganizacionNode: nodos del arbol en recorrido DFS.
        """

        yield self

        for hijo in self.hijos.values():
            yield from hijo
