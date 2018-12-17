import string
import random
import hashlib
import time

def uuid(size = 32, chars = string.ascii_uppercase + string.digits ):
	return ''.join(random.choice(chars) for _ in range(size))

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def get_time():
	t = time.localtime()
	return str(t.tm_hour) + ":" + str(t.tm_min) + ":" + str(t.tm_sec) + "  " + str(t.tm_mday) + "-" + str(t.tm_mon) + "-" + str(t.tm_year)
