from src.database.database import Database
from src.models.MetodoPreservacao.constantes import coleccao


class MetodoPreservacao(object):
    def __init__(self, metodo, idmetodo=None):
        self.metodo = metodo
        self.idmetodo = idmetodo

    def insert(self):
        data = MetodoPreservacao.find_by_name(self.metodo)
        if data is None:
            Database.insert(coleccao+'(metodo)', "'{}'".format(self.metodo))
            return True

        return False

    @staticmethod
    def find_by_name(metodo):
        data = Database.find_one_only('*', coleccao, " metodo='{}'".format(metodo))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idmetodo):
        data = Database.find_one('*', coleccao, "idmetododepreservacao={}".format(idmetodo))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idmetodo):
        Database.delete_one(coleccao, "idmetodo = {}".format(idmetodo))

    @staticmethod
    def editar(idmetodo, metodo):
        Database.update_one("metodo = '{}'".format(metodo), coleccao, "idmetodo = {}".format(idmetodo))
