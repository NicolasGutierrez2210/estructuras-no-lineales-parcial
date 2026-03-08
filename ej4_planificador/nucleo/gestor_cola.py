import heapq
from typing import List


class Tarea:
    def __init__(self, prioridad: int, timestamp: int, descripcion: str) -> None:
        self.prioridad = prioridad
        self.timestamp = timestamp
        self.descripcion = descripcion

    def __lt__(self, otra: "Tarea") -> bool:
        if self.prioridad == otra.prioridad:
            return self.timestamp < otra.timestamp
        return self.prioridad < otra.prioridad

    def __repr__(self) -> str:
        return f"Tarea(p={self.prioridad}, t={self.timestamp}, d='{self.descripcion}')"


class Planificador:
    def __init__(self) -> None:
        self.cola: List[Tarea] = []

    def agregar(self, tarea: Tarea) -> None:
        heapq.heappush(self.cola, tarea)

    def ejecutar(self) -> Tarea | None:
        if not self.cola:
            return None
        return heapq.heappop(self.cola)

    def vacio(self) -> bool:
        return len(self.cola) == 0
