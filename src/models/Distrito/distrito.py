from src.database.database import Database
from src.models.Distrito.constantes import coleccao

import uuid


class Distrito(object):
    def __init__(self, distrito, idprovincia, iddistrito=None):
        self.distrito = distrito
        self.iddistrito = iddistrito if not None else uuid.uuid4().int
        self.idprovincia = idprovincia

    def insert(self):
        data = Distrito.find_by_name(self.distrito)
        if data is None:
            Database.insert(coleccao+'(distrito,idprovincia)', "'{}',{}".format(self.distrito, self.idprovincia))
            return True

        return False

    @staticmethod
    def find_by_name(distrito):
        data = Database.find_one_only('*', coleccao, " distrito='{}'".format(distrito))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(iddistrito):
        data = Database.find_one_only('iddistrito, distrito', coleccao, " iddistrito= {}".format(iddistrito))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(iddistrito):
        Database.delete_one(coleccao, "iddistrito = {}".format(iddistrito))

    @staticmethod
    def editar(iddistrito, distrito):
        Database.update_one("distrito = '{}'".format(distrito), coleccao, "iddistrito = {}".format(iddistrito))
