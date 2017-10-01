from unittest import TestCase
from Main import Procesador


class TestProcesador(TestCase):
    def test_calcular_cadenavacia(self):
        self.assertEqual(Procesador.calcular("")[0], 0, "No son iguales")

    def test_calcular_tamanho1(self):
        self.assertEqual(Procesador.calcular("1")[0], 1, "No son iguales")

    def test_calcular_tamanho2(self):
            self.assertEqual(Procesador.calcular("1,2")[0], 2, "No son iguales")

    def test_calcular_tamanhoN(self):
            self.assertEqual(Procesador.calcular("1,2,3")[0], 3, "No son iguales")