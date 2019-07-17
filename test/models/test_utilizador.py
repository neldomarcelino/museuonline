from src.database.database import Database
from src.models.Utilizador.utilizador import Utilizador
import pytest


def test_registo():

    ret = Utilizador("neldo@digio.com", "digio+*12").register()
    assert False == ret
