from src.database.database import Database
from src.models.Genero.constantes import coleccao


class Genero(object):
    def __init__(self, genero, idfamilia, idgenero=None):
        self.genero = genero
        self.idgenero = idgenero
        self.idfamilia = idfamilia

    def insert(self):
        data = Genero.find_by_name(self.genero)

        if data is not None:
            if (d for d in data) == self.genero and (d for d in data) == self.idfamilia:
                return False
        Database.insert(coleccao+'(genero,idfamilia)', "'{}',{}".format(self.genero, self.idfamilia))
        return True

    @staticmethod
    def find_by_name(genero):
        data = Database.find_one_only('*', coleccao, " genero='{}'".format(genero))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idgenero):
        data = Database.find_one_only('*', coleccao, " idgenero= {}".format(idgenero))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idgenero):
        Database.delete_one(coleccao, "idgenero = {}".format(idgenero))

    @staticmethod
    def editar(idgenero, genero):
        Database.update_one("genero = '{}'".format(genero), coleccao, "idgenero = {}".format(idgenero))
