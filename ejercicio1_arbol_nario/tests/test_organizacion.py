import unittest
from src.organizacion_node import OrganizacionNode


class TestOrganizacion(unittest.TestCase):

    def test_estructura(self):

        rectoria = OrganizacionNode("Rectoria")

        rectoria.agregar_hijo("Ingenieria")
        rectoria.agregar_hijo("Medicina")

        ingenieria = rectoria.obtener_hijo("Ingenieria")
        ingenieria.agregar_hijo("Sistemas")

        nombres = [n.nombre for n in rectoria]

        self.assertIn("Rectoria", nombres)
        self.assertIn("Ingenieria", nombres)
        self.assertIn("Medicina", nombres)
        self.assertIn("Sistemas", nombres)


if __name__ == "__main__":
    unittest.main()
