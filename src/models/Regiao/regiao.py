from src.database.database import Database
from src.models.Regiao.constantes import coleccao
import uuid


class Regiao(object):
    def __init__(self, regiao, idregiao=None):
        self.regiao = regiao
        self.idregiao = uuid.uuid4().int

    def insert(self):
        data = Regiao.find_by_name(self.regiao)
        if data is None:
            Database.insert(coleccao+'(regiao)', "'{}'".format(self.regiao))
            return True

        return False

    @staticmethod
    def find_by_name(regiao):
        data = Database.find_one_only('*', coleccao, " regiao='{}'".format(regiao))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idregiao):
        data = Database.find_one_only('idregiao, regiao', coleccao, " idregiao= {}".format(idregiao))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idregiao):
        Database.delete_one(coleccao, "idregiao = {}".format(idregiao))

    @staticmethod
    def editar(idregiao, regiao):
        Database.update_one("regiao = '{}'".format(regiao), coleccao, "idregiao = {}".format(idregiao))
