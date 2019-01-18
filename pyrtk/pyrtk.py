
from cryptography.fernet import Fernet
from datetime import datetime
import json

        
# Requirements
def create_token(user_id, key):
    cipher_suite = Fernet(key)
    user_dic = {'user_id': user_id, 'created': datetime.today().timestamp()}
    
    encrypted_data = cipher_suite.encrypt(str.encode(json.dumps(user_dic))).decode("utf-8")

    return encrypted_data


def decode_token(token, key):
    cipher_suite = Fernet(key)
    try:
        key = eval(cipher_suite.decrypt(str.encode(rtk)).decode("utf-8"))
        return key
    except:
        return 'Incorrect token or key'


def generate_key():
    import base64
    import os

    # This key must be saved by the user to decode keys in the future
    return base64.urlsafe_b64encode(os.urandom(32))
