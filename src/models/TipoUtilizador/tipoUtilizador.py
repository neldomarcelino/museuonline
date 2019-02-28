from src.database.database import Database
from src.models.TipoUtilizador.constantes import coleccao

import uuid


class TipoUtilizador(object):
    def __init__(self, tipoutilizador, idtipoutilizador=None):
        self.tipoutilizador = tipoutilizador
        self.idtipoutilizador = uuid.uuid4().int

    def insert(self):
        data = TipoUtilizador.find_by_name(self.tipoutilizador)
        if data is None:
            Database.insert(coleccao+'(tipoutilizador)', "'{}'".format(self.tipoutilizador))
            return True

        return False

    @staticmethod
    def find_by_name(tipoutilizador):
        data = Database.find_one_only('*', coleccao, " tipoutilizador='{}'".format(tipoutilizador))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idtipoutilizador):
        data = Database.find_one_only('idtipoutilizador, tipoutilizador', coleccao, " idreino= {}".format(idtipoutilizador))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idtipoutilizador):
        Database.delete_one(coleccao, "idtipoutilizador = {}".format(idtipoutilizador))

    @staticmethod
    def editar(idtipoutilizador, tipoutilizador):
        Database.update_one("tipoutilizador = '{}'".format(tipoutilizador), coleccao, "idtipoutilizador = {}".format(idtipoutilizador))
