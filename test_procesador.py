from unittest import TestCase
from Main import Procesador


class TestProcesador(TestCase):
    def test_calcular_cadenavacia(self):
        self.assertEqual(Procesador.calcular(""), 0, "No son iguales")

    def test_calcular_tamanho1(self):
        self.assertEqual(Procesador.calcular("1"), 1, "No son iguales")

    def test_calcular_tamanho2(self):
            self.assertEqual(Procesador.calcular("1,2"), 2, "No son iguales")

