import random
import hashlib
import string
import base64

def gen_salt() -> str:
    return ''.join(random.sample(string.ascii_lowercase, 10))

def encrypt_password(password :str, salt :str):
    s = password + salt
    hash = hashlib.sha512(s.encode('utf-8'))
    s = str(base64.b64encode(hash.digest()), 'utf-8')
    return s
