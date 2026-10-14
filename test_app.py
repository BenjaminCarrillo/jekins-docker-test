import unittest

from app import saludar


class TestApp(unittest.TestCase):
    def test_saludo_por_defecto(self):
        self.assertEqual(saludar(), "Hola Mundo")

    def test_saludo_con_nombre(self):
        self.assertEqual(saludar("Duoc"), "Hola Duoc")


if __name__ == "__main__":
    unittest.main()
