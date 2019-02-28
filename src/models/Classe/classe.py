from src.database.database import Database
from src.models.Classe.constantes import coleccao


class Classe(object):
    def __init__(self, classe, idfilo, idclasse=None):
        self.classe = classe
        self.idfilo = idfilo
        self.idclasse = idclasse

    def insert(self):
        data = Classe.find_by_name(self.classe)

        if data is not None:
            if data[2] == self.idfilo and data[1] == self.classe:
                return False
        Database.insert(coleccao+'(classe,idfilo)', "'{}',{}".format(self.classe, self.idfilo))
        return True

    @staticmethod
    def find_by_name(classe):
        data = Database.find_one_only('*', coleccao, " classe='{}'".format(classe))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idclasse):
        data = Database.find_one_only('*', coleccao, " idclasse= {}".format(idclasse))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idclasse):
        Database.delete_one(coleccao, "idclasse = {}".format(idclasse))

    @staticmethod
    def editar(idclasse, classe):
        Database.update_one("classe = '{}'".format(classe), coleccao, "idclasse = {}".format(idclasse))
