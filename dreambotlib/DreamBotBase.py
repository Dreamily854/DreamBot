import hashlib

def hashmd5(data):
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()