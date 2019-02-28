from src.models.Pessoa.constantes import coleccao
from src.database.database import Database


class Pessoa(object):
    def __init__(self, nome, idpessoa=None):
        self.idpessoa = idpessoa
        self.nome = nome

    def insert(self):
        data = Pessoa.find_by_name(self.nome)
        if data is None:
            Database.insert(coleccao+'(nome)', "'{}'".format(self.nome))
            return True

        return False

    @staticmethod
    def find_by_name(nome):
        data = Database.find_one_only('*', coleccao, " nome='{}'".format(nome))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idpessoa):
        data = Database.find_one('*', coleccao, "idpessoa={}".format(idpessoa))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idpessoa):
        Database.delete_one(coleccao, "idpessoa = {}".format(idpessoa))

    @staticmethod
    def editar(idpessoa, nome):
        Database.update_one("nome = '{}'".format(nome), coleccao, "idpessoa = {}".format(idpessoa))
