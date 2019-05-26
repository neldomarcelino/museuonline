from src.config import ADMINS
from src.database.database import Database
from src.models.Utilizador.constantes import coleccao,pedido
from src.database.utils import Utils
import pytest
from email.message import EmailMessage,errors
import smtplib


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
        Database.update_one(
            "email = '{}' and password = '{}'".format(email, password), coleccao, "idutilizador = {}".format(idutilizador)
        )

    @staticmethod
    def recuperar_password(utilizador):
        return Utilizador.send_email(utilizador[1], utilizador[2])

    @staticmethod
    def send_email(email_destino, password):
        email = EmailMessage()
        email['Subject'] = "Recuperacao de Password MuseuOnline Unilurio"
        email['From'] = 'gfernando@unilurio.ac.mz'
        email['To'] = email_destino
        try:
            email.set_content(
                "Recuperacao do password, utilize o link: {}, para recuperar sua conta no Museu Online UniLurio"
                "\n\n!".format("facebook.com/"+password)
            )

            smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)

            smtp.starttls()
            smtp.login("gfernando@unilurio.ac.mz", "#G!g!l+*12.")

            smtp.send_message(email)
            smtp.quit()

        except smtplib.SMTPConnectError:
            return smtplib.SMTPConnectError("123", "Conexao failed")

        except smtplib.SMTPAuthenticationError:
            return smtplib.SMTPAuthenticationError("124","Erro de autenticacao")

        except smtplib.SMTPServerDisconnected:
            return smtplib.SMTPServerDisconnected

        except smtplib.SMTPDataError:
            return "Error"

        except smtplib.SMTPSenderRefused:
            return smtplib.SMTPSenderRefused("126", "Error send refused", email['To'])

        except smtplib.SMTPResponseException:
            return smtplib.SMTPResponseException("125", "Error not Respponse")

        except smtplib.SMTPNotSupportedError:
            return "error Not supported"

        except smtplib.SMTPException:
            return "ERRORR"
