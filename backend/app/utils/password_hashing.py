import bcrypt

#encrypt the password using bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

#verifying the password
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)