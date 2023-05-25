import requests

import logging

HOST = 'http://127.0.0.1:5000'


def send(command, **kwargs):
    msg = f'{HOST}/{command}'
    logging.debug(msg)
    r = requests.post(msg, json={key: value for key, value in kwargs.items()})
    return r.json()