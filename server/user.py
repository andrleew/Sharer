# coding=utf-8

from user_device import TUserDevice

class TUser():
    user_id: int
    login: str
    password: str
    devices: list
    updates: dict

    def __init__(self, user_id, login, password, devices=[], updates={}):
        self.user_id = user_id
        self.login = login
        self.password = password
        self.devices = devices
        self.updates = updates
        