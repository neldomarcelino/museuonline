import mysql
from mysql.connector import connect, errorcode, errors
from src.database.configDB import config
import src.database.error as errorDB
import uuid


class Database(object):
    connect_db = None
    cursor = None

    @staticmethod
    def connection():
        try:
            Database.connect_db = connect(**config)
            Database.cursor = Database.connect_db.cursor()
        except mysql.connector.ProgrammingError as err:
            errorDB.connectionError("Erro de conexacao com a base de dados")

    @staticmethod
    def insert(coleccao, data):

        try:
            my_query = "insert into {} values ({})".format(coleccao, data)
            Database.cursor.execute(my_query)
        except mysql.connector.ProgrammingError as err:
            if err.errno == errorcode.ER_SYNTAX_ERROR:
                errorDB.syntaxError("Erro de sintaxe, verfique a consulta SQL!!")
            return None

        except AttributeError:
            print("Bugs Insert: {}".format(AttributeError.args))

        except errors.OperationalError as e:
            print("Many connection--{}".format(e.msg))

        finally:
            Database.connect_db.cmd_reset_connection()

    @staticmethod
    def find_one(atributo, coleccao, condicao):
        try:
            my_query = "select {} from {} where {}".format(atributo, coleccao, condicao)
            Database.cursor.execute(my_query)
            return Database.cursor.fetchall()
        except mysql.connector.ProgrammingError as err:
            if err.errno == errorcode.ER_SYNTAX_ERROR:
                errorDB.syntaxError("Erro de sintaxe, verfique a consulta SQL!!")
            return None
        finally:
            Database.connect_db.cmd_reset_connection()


    @staticmethod
    def find_group(atributo, coleccao, group):
        try:
            my_query = "select {} from {} group by {}".format(atributo, coleccao, group)
            Database.cursor.execute(my_query)
            return Database.cursor.fetchall()


        except mysql.connector.ProgrammingError as err:
            if err.errno == errorcode.ER_SYNTAX_ERROR:
                errorDB.syntaxError("Erro de sintaxe, verfique a consulta SQL!!")

        except mysql.connector.errors.DatabaseError as e:
            print("==========++++++@@@@@@@@@@@@@@@@@{}".format(e.msg))

        finally:
            Database.connect_db.cmd_reset_connection()

    @staticmethod
    def find_one_only(atributo, coleccao, condicao):
        try:
            my_query = "select {} from {} where {}".format(atributo, coleccao, condicao)
            Database.cursor.execute(my_query)
            return Database.cursor.fetchone()
        except mysql.connector.ProgrammingError as err:
            if err.errno == errorcode.ER_SYNTAX_ERROR:
                errorDB.syntaxError("Erro de sintaxe, verfique a consulta SQL!!")
                return None
        except mysql.connector.errors.DatabaseError as e:
            print("{}".format(e.msg))
            return None

        except AttributeError:
            print("Bugs:  {}".format(AttributeError))

            return None
        finally:
            Database.connect_db.cmd_reset_connection()

    @staticmethod
    def find(atributo, coleccao):
        try:
            my_query = "select {} from {}".format(atributo, coleccao)
            Database.cursor.execute(my_query)
            return Database.cursor.fetchall()
        except mysql.connector.ProgrammingError as err:
            if err.errno == errorcode.ER_SYNTAX_ERROR:
                errorDB.syntaxError("Erro de sintaxe, verfique a consulta SQL!!")
        finally:
            Database.connect_db.cmd_reset_connection()

    @staticmethod
    def update_one(atributo, colleccao, condicao):
        try:
            my_query = "update {} set {} where {}".format(colleccao, atributo, condicao)
            Database.cursor.execute(my_query)
        except mysql.connector.ProgrammingError as err:
            if err.errno == errorcode.ER_SYNTAX_ERROR:
                errorDB.syntaxError("Erro de sintaxe, verfique a consulta SQL!!")
        finally:
            Database.connect_db.cmd_reset_connection()

    @staticmethod
    def update_all(atributo, colleccao):
        try:
            my_query = "update {} set {}".format(colleccao, atributo)
            Database.cursor.execute(my_query)
        except mysql.connector.ProgrammingError as err:
            if err.errno == errorcode.ER_SYNTAX_ERROR:
                errorDB.syntaxError("Erro de sintaxe, verfique a consulta SQL!!")

    @staticmethod
    def delete_all(coleccao):
        try:
            my_query = "delete {}".format(coleccao)
            Database.cursor.execute(my_query)
        except mysql.connector.ProgrammingError as err:
            if err.errno == errorcode.ER_SYNTAX_ERROR:
                errorDB.syntaxError("Erro de sintaxe, verfique a consulta SQL!!")

    @staticmethod
    def delete_one(coleccao, condicao):
        try:
            my_query =  "delete from {} where {}".format(coleccao,condicao)
            Database.cursor.execute(my_query)
        except mysql.connector.ProgrammingError as err:
            if err.errno == errorcode.ER_SYNTAX_ERROR:
                errorDB.syntaxError("Erro de sintaxe, verfique a consulta SQL!!")

