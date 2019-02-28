from src.database.database import Database
from src.models.Ordem.constantes import coleccao


class Ordem(object):
    def __init__(self, ordem, idclasse, idordem=None):
        self.ordem = ordem
        self.idordem = idordem
        self.idclasse = idclasse

    def insert(self):
        data = Ordem.find_by_name(self.ordem)

        if data is not None:
            if data[2] == self.idordem and data[1] == self.ordem:
                return False
        Database.insert(coleccao+'(ordem,idclasse)', "'{}',{}".format(self.ordem, self.idclasse))
        return True

    @staticmethod
    def find_by_name(ordem):
        data = Database.find_one_only('*', coleccao, " ordem='{}'".format(ordem))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idordem):
        data = Database.find_one_only('*', coleccao, " idordem= {}".format(idordem))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idordem):
        Database.delete_one(coleccao, "idordem = {}".format(idordem))

    @staticmethod
    def editar(idordem, ordem):
        Database.update_one("ordem = '{}'".format(ordem), coleccao, "idordem = {}".format(idordem))