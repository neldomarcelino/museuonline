from src.config import ADMINS
from src.database.database import Database
from src.models.Utilizador.constantes import coleccao,pedido
from src.database.utils import Utils


class Utilizador(object):
    def __init__(self, email, password, idtipoutilizador=None, idutilizador=None):
        self.idutilizador = idutilizador
        self.email = email
        self.password = Utils.hash_password(password)
        self.idtipoutilizador = idtipoutilizador

    def register(self):
        data = Utilizador.find_by_email(self.email)

        if data is None:
            Database.insert(coleccao+'(email,senha,idtipoutilizador)', "'{}','{}','{}'".format(self.email, self.password, self.idtipoutilizador))
            return True
        return False

    def pedido(self):
        data = Utilizador.find_by_email(self.email)

        if data is None:
            Database.insert(pedido+'(email,password)', "'{}','{}'".format(self.email, self.password))
            return True
        return False

    @staticmethod
    def is_login_valid(email, password):
        user_data = Database.find_one_only("*", coleccao, "email = '{}'".format(email))
        if user_data is not None:
            if Utils.check_hashed_password(password, user_data[2]):
                return True
        if email in ADMINS:
            return True
        return False

    @staticmethod
    def find_by_email(email):
        data = Database.find_one_only('*', coleccao, " email='{}'".format(email))

        if data is not None:
            return data

    @staticmethod
    def find_by_id(idutilizador):
        data = Database.find_one_only('*', coleccao, " idutilizador= {}".format(idutilizador))
        if data is not None:
            return data

    @staticmethod
    def find_pesquisa(email):
        data = Database.find_one('*', coleccao, " email like '%{}%'".format(email))
        if data is not None:
            return data

    @staticmethod
    def find_all():
        data = Database.find('*', coleccao)
        if data is not None:
            return data

    @staticmethod
    def delete(idutilizador):
        Database.delete_one(coleccao, "idutilizador = {}".format(idutilizador))

    @staticmethod
    def editar(idutilizador, email, password):
        Database.update_one("email = '{}' and password = '{}'".format(email, password), coleccao, "idutilizador = {}".format(idutilizador))
