from src.models.LocalizacaoEspecie.constantes import coleccao
from src.models.Especie.constantes import coleccao as especiecoleccao
from src.models.Distrito.constantes import coleccao as distritocoleccao
from src.models.Distrito.distrito import Distrito
from src.models.Especie.especie import Especie
from src.database.database import Database


class LocalizacaoEspecie(object):
    def __init__(self, distrito, idespecie, idlocalizacao=None):
        self.distrito = distrito
        self.idespecie = idespecie
        self.idlocalizacao = idlocalizacao

    def insert(self):
        iddistrito = Distrito.find_by_name(self.distrito)
        idespecie = Especie.find_by_id(self.idespecie)

        if iddistrito is None:
            Distrito(self.distrito, 4).insert()
            iddistrito = Distrito.find_by_name(self.distrito)

        if idespecie is None:
            Especie(self.idespecie).insert()
            idespecie = Especie.find_by_name(self.idespecie)

        Database.insert(coleccao+'(iddistrito, idespecie)', "{}, {}".format(iddistrito[0], self.idespecie))
        return True

    @staticmethod
    def find_by_distrito_id(iddistrito):
        data = Database.find_one('idespecie,especie',
                                      coleccao+','+especiecoleccao,
                                      "{}.idEspecie = {}.idEspecie and {}.iddistrito= {}".format(especiecoleccao, coleccao, coleccao, iddistrito))
        if data is not None:
            return data

    @staticmethod
    def find_by_especie_id(idespecie):
        data = Database.find_one('idistrito, distrito',
                                      coleccao+','+distritocoleccao,
                                      "{}.iddistrito = {}.iddistrito and {}.idespecie= {}".format(distritocoleccao, coleccao, coleccao, idespecie))

        if data is not None:
            return data

    @staticmethod
    def find_by_distrito_name(distrito):
        distrito_d = Distrito.find_by_name(distrito)

        data = Database.find_one('idespecie,especie',
                                 coleccao + ',' + especiecoleccao,
                                 "{}.idEspecie = {}.idEspecie and {}.iddistrito= {}".format(especiecoleccao, coleccao,
                                                                                            coleccao, distrito_d[0]))
        if data is not None:
            return data

    @staticmethod
    def find_by_especie_name(especie):
        data = Database.find_one('idistrito, distrito',
                                 coleccao + ',' + distritocoleccao,
                                 "{}.iddistrito = {}.iddistrito and {}.idespecie= {}".format(distritocoleccao, coleccao,
                                                                                             coleccao, especie))

        if data is not None:
            return data
    @staticmethod
    def delete(idlocalizacao):
        Database.delete_one(coleccao, "idlocalizacao = {}".format(idlocalizacao))

    @staticmethod
    def editar(idlocalizacao,iddistrito, idespecie):
        Database.update_one("iddistrito = {} and idespecie = {}".format(iddistrito, idespecie), coleccao, "idlocalizacao = {}".format(idlocalizacao))


