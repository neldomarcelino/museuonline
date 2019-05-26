import unittest
from src.models.Utilizador.utilizador import Utilizador


class utilizador_testes(unittest.TestCase):

    def configure(self):
        self.assertEqual(Utilizador.recuperar_password(), "neldo@digio.com")
