from flask import Flask, request, jsonify

from user import TUser
from user_device import TUserDevice
from database_manager import TDatabaseManager

app = Flask(__name__)
db = TDatabaseManager()
users_by_logins: dict = None
users_by_ids: dict = None

@app.route('/sign_up', methods=['POST'])
def sign_up():
    # login, password
    content = request.json
    login = content['login']
    password = content['password']

    if login in users_by_logins.keys() or not login or not password:
        return jsonify(status=1)
    else:
        user = db.make_new_user(login, password)
        users_by_logins[login] = user
        return jsonify(status=0, id=user.user_id)

@app.route('/sign_in', methods=['POST'])
def sign_in():
    #login, password
    content = request.json
    login = content['login']
    password = content['password']

    if login in users_by_logins.keys() and users_by_logins[login].password == password:
        return jsonify(status=0, id=users_by_logins[login].user_id)
    else:
        return jsonify(status=1)

@app.route('/', methods=['POST', 'GET'])
def main():
    return 'hello, world'

def get_users_by_ids(users_by_logins: dict):
    users = dict()
    for user in users_by_logins.values():
        users[user.user_id] = user
    return users

if __name__ == '__main__':
    users_by_logins = db.get_users()
    users_by_ids = get_users_by_ids(users_by_logins)
    app.run()
