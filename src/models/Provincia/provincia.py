import uuid

from src.database.database import Database
from src.models.Provincia.constantes import coleccao
from src.models.Regiao.regiao import Regiao


class Provincia(object):
    def __init__(self, provincia, idregiao, idprovincia=None):
        self.provincia = provincia
        self.idregiao = idregiao
        self.idprovincia = idprovincia if not None else uuid.uuid4().int

    def insert(self):
        data = Provincia.find_by_name(self.provincia)
        if data is None:
            Database.insert(coleccao+'(provincia,idregiao)', "'{}',{}".format(self.provincia, self.idregiao))
            return True

        return False

    @staticmethod
    def find_by_name(provincia):
        data = Database.find_one_only('*', coleccao, " provincia='{}'".format(provincia))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idprovincia):
        data = Database.find_one_only('idprovincia, provincia', coleccao, " idprovincia= {}".format(idprovincia))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idprovincia):
        Database.delete_one(coleccao, "idprovincia = {}".format(idprovincia))

    @staticmethod
    def editar(idprovincia, provincia):
        Database.update_one("provincia = '{}'".format(provincia), coleccao, "idprovincia = {}".format(idprovincia))

