# Module pour authentification sécurisée
import bcrypt
import json
import os

def authenticate_user(username, password):
    users_file = 'data/users.json'
    if not os.path.exists(users_file):
        return False
    with open(users_file, 'r') as f:
        users = json.load(f)
    if username in users:
        return bcrypt.checkpw(password.encode(), users[username].encode())
    return False
