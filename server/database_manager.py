# -*- coding: utf-8 -*-

import psycopg2
from user import TUser

DB_NAME = 'Sharer'
LOGIN = 'ShareServer'
PASSWORD = 1234

class TDatabaseManager():
    ACCOUNTS = 'accounts'

    _database = None
    _cursor = None

    def __init__(self):
        pass

    @property
    def database(self):
        if not self._database:
            self._database = psycopg2.connect(f"dbname={DB_NAME} user={LOGIN} password={PASSWORD}")
        return self._database

    @property
    def cursor(self):
        if not self._cursor:
            self._cursor = self.database.cursor()
        return self._cursor

    def make_new_user(self, login, password):
        self.cursor.execute(f"insert into {self.ACCOUNTS} (login, password) values (%s, %s);", (login, password))
        self.cursor.execute(f"select id_client from {self.ACCOUNTS} where login = %s limit 1;", (login,))
        user_id = self.cursor.fetchone()[0]
        return TUser(user_id=user_id, login=login, password=password)

    def get_users(self) -> dict:
        self.cursor.execute(f"select id_client, login, password from {self.ACCOUNTS};")
        users = dict()
        for id_client, login, password in self.cursor.fetchall():
            users[login] = TUser(user_id=id_client, login=login, password=password)
        return users
