from src.database.database import Database
from src.models.Reino.constantes import coleccao

import uuid


class Reino(object):
    def __init__(self, reino, idreino=None):
        self.reino = reino
        self.idreino = uuid.uuid4().int

    def insert(self):
        data = Reino.find_by_name(self.reino)
        if data is None:
            Database.insert(coleccao+'(reino)', "'{}'".format(self.reino))
            return True

        return False

    @staticmethod
    def find_by_name(reino):
        data = Database.find_one_only('*', coleccao, " reino='{}'".format(reino))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idreino):
        data = Database.find_one_only('idreino, reino', coleccao, " idreino= {}".format(idreino))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idreino):
        Database.delete_one(coleccao, "idreino = {}".format(idreino))

    @staticmethod
    def editar(idreino, reino):
        Database.update_one("reino = '{}'".format(reino), coleccao, "idreino = {}".format(idreino))
