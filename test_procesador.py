from unittest import TestCase
from Main import Procesador


class TestProcesador(TestCase):
    def test_calcular(self):
        self.assertEqual(Procesador.calcular(), 0, "No son iguales")
