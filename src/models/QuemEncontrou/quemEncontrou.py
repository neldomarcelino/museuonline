from src.database.database import Database
from src.models.QuemEncontrou.constantes import coleccao
from src.models.Pessoa.pessoa import Pessoa
from src.models.Especie.especie import Especie


class QuemEncontrou(object):
    def __init__(self, pessoa, idespecie):
        self.idespecie = idespecie
        self.pessoa = pessoa

    def insert(self):
        idpessoa = Pessoa.find_by_name(self.pessoa)
        idespecie = Especie.find_by_id(self.idespecie)

        verfica = False

        if idpessoa is None:
            Pessoa(self.pessoa).insert()
            idpessoa = Pessoa.find_by_name(self.pessoa)
            verfica = True

        if idespecie is None:
            Especie(self.idespecie).insert()
            idespecie = Especie.find_by_id(self.idespecie)
            verfica = True

        if verfica:
            Database.insert(coleccao+'(idpessoa, idespecie)', "{}, {}".format(idpessoa[0], self.idespecie))
        return True

    @staticmethod
    def find_by_idespecie_idpessoa(idpessoa, idespecie):
        data = Database.find_one_only('*', coleccao, "idpessoa={} and idespecie={}".format(idpessoa, idespecie))
        if data is not None:
            return data

    @staticmethod
    def find_pessoa(idpessoa):
        data = Pessoa.find_by_id(idpessoa)
        if data is not None:
            return data

    @staticmethod
    def find_especie(idespecie):
        data = Especie.find_by_id(idespecie)
        if data is not None:
            return data

    @staticmethod
    def find_pessoa_especie(idespecie):
        pessoa=0
        data = Database.find_one("*", coleccao, "idespecie={}".format(idespecie))
        if data is not None:
            for (idpessoa, idespec) in data:
                pessoa = idpessoa

            data = QuemEncontrou.find_pessoa(pessoa)
            for (idpessoa, nome) in data:
                pessoa = nome

            return pessoa

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idreino):
        Database.delete_one(coleccao, "idreino = {}".format(idreino))

    @staticmethod
    def editar(idreino, reino):
        Database.update_one("reino = '{}'".format(reino), coleccao, "idreino = {}".format(idreino))

