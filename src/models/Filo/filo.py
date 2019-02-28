from src.database.database import Database
from src.models.Filo.constantes import coleccao
from src.models.Reino.reino import Reino

import uuid


class Filo(object):
    def __init__(self, filo, idreino, idfilo=None):
        self.filo = filo
        self.idfilo = uuid.uuid4().int
        self. idreino = idreino

    def insert(self):
        data = Filo.find_by_name(self.filo)

        if data is not None:
            if data[2] == self.idreino and data[1] == self.filo:
                return False
        Database.insert(coleccao+'(filo,idreino)', "'{}',{}".format(self.filo, self.idreino))
        return True

    @staticmethod
    def buscar_reino(reino):
        ret_reino = Reino.find_by_name(reino)

        if ret_reino is not None:
            data = Database.find_one('idFilo, filo', coleccao, " idReino= {} ".format(ret_reino[0]))
            if data is not None:
                return data

    @staticmethod
    def find_by_name(filo):
        data = Database.find_one_only('*', coleccao, " filo='{}'".format(filo))

        if data is not None:
            return data

    @staticmethod
    def find_by_id(idfilo):
        data = Database.find_one_only('*', coleccao, " idfilo= {}".format(idfilo))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idfilo):
        Database.delete_one(coleccao, "idfilo = {}".format(idfilo))

    @staticmethod
    def editar(idfilo, filo):
        Database.update_one("filo = '{}'".format(filo), coleccao, "idfilo = {}".format(idfilo))
    
