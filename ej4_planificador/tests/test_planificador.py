import unittest
from nucleo.gestor_cola import Tarea, Planificador


class TestPlanificador(unittest.TestCase):

    def setUp(self) -> None:
        self.sistema = Planificador()

    def test_agregar_y_ejecutar(self) -> None:
        t1 = Tarea(3, 1, "proceso_A")
        t2 = Tarea(1, 2, "proceso_B")

        self.sistema.agregar(t1)
        self.sistema.agregar(t2)

        resultado = self.sistema.ejecutar()

        self.assertEqual(resultado.descripcion, "proceso_B")

    def test_misma_prioridad(self) -> None:
        t1 = Tarea(1, 1, "proceso_A")
        t2 = Tarea(1, 2, "proceso_B")

        self.sistema.agregar(t1)
        self.sistema.agregar(t2)

        resultado = self.sistema.ejecutar()

        self.assertEqual(resultado.descripcion, "proceso_A")


if __name__ == "__main__":
    unittest.main()
