from src.models.Familia.constantes import coleccao
from src.database.database import Database


class Familia(object):
    def __init__(self, familia, idordem, idfamilia=None):
        self.familia = familia
        self.idordem = idordem
        self.idfamilia = idfamilia

    def insert(self):
        data = Familia.find_by_name(self.familia)

        if data is not None:
            if (d for d in data) == self.familia and (d for d in data) == self.idordem:
                return False
        Database.insert(coleccao+'(familia,idordem)', "'{}',{}".format(self.familia, self.idordem))
        return True

    @staticmethod
    def find_by_name(familia):
        data = Database.find_one_only('*', coleccao, " familia='{}'".format(familia))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idfamilia):
        data = Database.find_one_only('*', coleccao, " idfamilia= {}".format(idfamilia))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idfamilia):
        Database.delete_one(coleccao, "idfamilia = {}".format(idfamilia))

    @staticmethod
    def editar(idfamilia, familia):
        Database.update_one("familia = '{}'".format(familia), coleccao, "idfamilia = {}".format(idfamilia))
