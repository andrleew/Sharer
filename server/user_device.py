# -*- coding: utf-8 -*-

class TUserDevice():
    device_id: int
    user_id: int
    device_name: str

    def __init__(self, device_id, user_id, device_name):
        self.device_id = device_id
        self.user_id = user_id
        self.device_name = device_name
