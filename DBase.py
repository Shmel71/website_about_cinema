import sqlite3


class ConnectToDb:
    def __init__(self, connect: sqlite3.Connection) -> None:
        self.__connect = connect
        self.__cursor = connect.cursor()

    def get_film_content(self):
        SQL = """SELECT * FROM films_content"""
        try:
            self.__cursor.execute(SQL)
            return self.__cursor.fetchall()
        except:
            print("Ошибка чтения базы данных.")
            return []

    def get_film(self, film_id):
        SQL = """SELECT * FROM films_content WHERE id = ?"""
        try:
            self.__cursor.execute(SQL, (film_id,))
            return self.__cursor.fetchone()
        except:
            print("Ошибка чтения базы данных.")
            return []
