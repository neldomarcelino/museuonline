import uuid

from src.database.database import Database
from src.models.Especie.constantes import coleccao,coleccao_taxinomia,taxinomia_consulta


class Especie(object):
    def __init__(self, especie, idgenero=None, habitat=None, coordenadas=None, notas=None, detalhes=None,
                 nomecomum=None, validacao=None, datacriacao=None):
        self.especie = especie
        self.idgenero = idgenero
        self.habitat = habitat
        self.coordenadas = coordenadas
        self.notas = notas
        self.detalhes = detalhes
        self.nomecomum = nomecomum
        self.codigo = uuid.uuid4().hex
        self.validacao = validacao
        self.datacriacao = datacriacao

    def insert(self):
        Database.insert(coleccao+"(especie, idgenero, habitat, coordenadas, notas, detalhes,"+
                        "nomecomum, codigo, validacao, datacriacao)",
                        "'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}'"
                        .format(self.especie, self.idgenero, self.habitat, self.coordenadas, self.notas, self.detalhes,
                                self.nomecomum, self.codigo, self.validacao, self.datacriacao))
        return self.codigo

    @staticmethod
    def find_by_name(especie):
        data = Database.find_one('*', coleccao, " especie='{}'".format(especie))
        if data is not None:
            return data

    @staticmethod
    def find_pesquisa(especie):
        data = Database.find_one('*', coleccao, " especie like '%{}%'".format(especie))
        if data is not None:
            return data

    @staticmethod
    def find_by_id(idespecie):

        data = Database.find_one('*', coleccao, " idespecie= {}".format(idespecie))
        if data is not None:
            return data

    @staticmethod
    def find_taxinomia(idespecie, idgenero):

        data = Database.find_one('Especie, Genero, Familia, Ordem, Classe, Filo, Reino',
                                 coleccao_taxinomia, " especie.idespecie= {} and genero.idgenero = {} and {}".format(idespecie,idgenero,taxinomia_consulta))
        if data is not None:
            return data

    @staticmethod
    def find_by_id_nome(idespecie):
        especie = ""
        data = Database.find_one('*', coleccao, " idespecie= {}".format(idespecie))
        if data is not None:
            for (idespecie, especie, genero, habitat, coordenadas, notas, detalhes, nomecomum, codigo, validacao,
                datacriacao) in data:
                especie = especie
            return especie

    @staticmethod
    def find_by_codigo(codigo):
        idespeci=1
        data = Database.find_one('*', coleccao, " codigo= '{}'".format(codigo))
        if data is not None:
            for (idespecie, especie, genero, habitat, coordenadas, notas, detalhes, nomecomum, codigo, validacao,
                 datacriacao) in data:
                idespeci = idespecie
            return idespeci

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idespecie):
        Database.delete_one(coleccao, "idespecie = {}".format(idespecie))

    @staticmethod
    def editar(idespecie, especie, genero=None, habitat=None,coordenadas=None,
               notas=None, detalhes=None, nomecomum=None, codigo=None, validacao=None):
        Database.update_one("especie = '{}'".format(especie), coleccao, "idespecie = {}".format(idespecie))
