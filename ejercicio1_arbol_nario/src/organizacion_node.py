from __future__ import annotations
from typing import Dict, Iterator


class OrganizacionNode:

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.hijos: Dict[str, OrganizacionNode] = {}

    def agregar_hijo(self, nombre: str) -> None:
        if nombre not in self.hijos:
            self.hijos[nombre] = OrganizacionNode(nombre)

    def obtener_hijo(self, nombre: str) -> OrganizacionNode:
        if nombre not in self.hijos:
            raise KeyError("Hijo no encontrado")
        return self.hijos[nombre]

    def __iter__(self) -> Iterator["OrganizacionNode"]:
        yield self
        for hijo in self.hijos.values():
            yield from hijo
