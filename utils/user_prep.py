from passlib.hash import pbkdf2_sha256


def prepare_user_to_save(user):
    prepared_user = dict(user)
    prepared_user["password"] = pbkdf2_sha256.hash(prepared_user["password"])
    del prepared_user["id"]
    return prepared_user

""" user=prepare_user_to_save({'id':None,'full_name':'some name', 'email':'some email','password':'secret'})
print(user) """

def decryp_password(password,sha_pass):
    r = pbkdf2_sha256.verify(password, sha_pass)
    if not r:
        return 'Invalid Password'
    else:
        return True 