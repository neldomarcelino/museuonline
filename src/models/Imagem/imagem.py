from src.database.database import Database
from src.models.Imagem.coleccao import coleccao,path_image
from src.models.Especie.especie import Especie
from werkzeug.utils import redirect,secure_filename
import os
import glob


class Imagem(object):
    def __init__(self, imagem, idespecie, idimagem=None):
        self.imagem = imagem
        self.idImagem = idimagem
        self.idespecie = idespecie

    def insert(self):
        Database.insert(coleccao+'(imagem, idespecie)', "'{}', {}".format(self.imagem, self.idespecie))

    @staticmethod
    def imagem_processamento(imagem, idespecie):
        data = Especie.find_by_id(idespecie)
        path = path_image+"/{}".format(idespecie)

        if data is not None:
            if not os.path.exists(path):
                os.mkdir(path)

            ultima_image = Imagem.find_last_image()
            imagem.save(path+"/{}.png".format(int(ultima_image[0])+1))
            Imagem(path+"/{}".format(int(ultima_image[0])+1), idespecie).insert()

        return True

    @staticmethod
    def find_by_id(idimagem):
        data = Database.find_one_only('*', coleccao, " idimagem= {}".format(idimagem))
        if data is not None:
            return data

    @staticmethod
    def find_last_image():
        id=0
        data = Database.find('max(idimagem)', coleccao)
        if data is not None:
            for idimagem in data:
                id = idimagem

            return id
        return 0

    @staticmethod
    def especie_imagem(especie):
        path = path_image+"/{}".format(especie)
        if os.path.exists(path):
            return glob.glob(path+"/*")

    @staticmethod
    def find_all():
        data = None#Database.find_group('MAX(idImagem) idImagem, idEspecie', coleccao,'idEspecie')
        if data is not None:
            return data

    @staticmethod
    def delete(idimagem):
        Database.delete_one(coleccao, "idimagem = {}".format(idimagem))

    @staticmethod
    def editar(idimagem, imagem):
        Database.update_one("imagem = '{}'".format(imagem), coleccao, "idimagem = {}".format(idimagem))

    @staticmethod
    def all_img_path(idespecie):
        names = glob.glob(path_image+"/{}/*".format(idespecie))
        return names


#names = Imagem.all_img_path(34)
#for name in names:
#    print(name.split("/")[name.split("/").__len__()-1])