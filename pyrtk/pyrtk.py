
from cryptography.fernet import Fernet
from datetime import datetime
import json

        
def create_token(user_dic, key):
    cipher_suite = Fernet(key)

    return cipher_suite.encrypt(str.encode(json.dumps(user_dic))).decode("utf-8")


def decode_token(token, key):
    cipher_suite = Fernet(key)
    
    try:
        key = eval(cipher_suite.decrypt(str.encode(token)).decode("utf-8"))
        return key
    except:
        return 'Incorrect token or key'


def generate_key():
    import base64
    import os

    # This key must be saved by the user to decode keys in the future
    return base64.urlsafe_b64encode(os.urandom(32))
