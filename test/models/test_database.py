from src.database.configDB import config
from mysql.connector import connect


cursor = None


def test_connetion():

    with connect(**config) as db:
        cursor = db.cursor()

    yield test_connetion()

    db.close()

    assert cursor == None

