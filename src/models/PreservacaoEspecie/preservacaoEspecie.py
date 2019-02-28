from src.database.database import Database
from src.models.PreservacaoEspecie.constantes import coleccao
from src.models.MetodoPreservacao.metodoPreservacao import MetodoPreservacao
from src.models.Especie.especie import Especie


class PreservacaoEspecie(object):
    def __init__(self, idespecie, metodopreservacao, preservacaoespecie=None):
        self.idespecie = idespecie
        self.metodopreservacao = metodopreservacao
        self.preservacaoespecie = preservacaoespecie

    def insert(self):
        idespecie = Especie.find_by_id(self.idespecie)
        idmetodopreservacao = MetodoPreservacao.find_by_name(self.metodopreservacao)

        if idespecie is None:
            Especie(self.idespecie).insert()
            idespecie = Especie.find_by_name(self.idespecie)

        if idmetodopreservacao is None:
            MetodoPreservacao(self.metodopreservacao).insert()
            idmetodopreservacao = MetodoPreservacao.find_by_name(self.metodopreservacao)

        Database.insert(coleccao+'(idmetododepreservacao, idespecie)', "{}, {}".format(idmetodopreservacao[0], self.idespecie))
        return True

    @staticmethod
    def find_by_idespecie_idpessoa(idpessoa, idespecie):
        data = Database.find_one_only('*', coleccao, " idpessoa={} and idespecie={}".format(idpessoa, idespecie))
        if data is not None:
            return data

    @staticmethod
    def find_metodo(idmetodo):
        data = MetodoPreservacao.find_by_id(idmetodo)
        if data is not None:
            return data

    @staticmethod
    def find_especie(idespecie):
        data = Especie.find_by_id(idespecie)
        if data is not None:
            return data

    @staticmethod
    def find_pessoa_especie(idespecie):
        metodo = ''
        data = Database.find_one("*", coleccao, "idespecie={}".format(idespecie))
        if data is not None:
            for (idpreservacao, idmetodo, idespec) in data:
                metodo = idmetodo

            data = PreservacaoEspecie.find_metodo(metodo)
            if data is not None:
                for (idmetodo, method) in data:
                    metodo = method
                return metodo

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
