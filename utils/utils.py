import hashlib


def md5(value):
    return hashlib.md5(str(value).encode()).hexdigest()