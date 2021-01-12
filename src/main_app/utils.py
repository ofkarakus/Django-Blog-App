import uuid


def get_random_uid():
    uid = str(uuid.uuid4())[:11].replace('-', '')
    return uid
