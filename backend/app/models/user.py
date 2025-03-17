from app.utils.password_hashing import hash_password
from app import db

class User:
    #initialize a User instance with email and #password
    def __init__(self, email, password):
        self.email = email
        self.password = hash_password(password)
        
    #save the user instance data to the database and return the inserted ID
    def save(self, db):
        user_data = {
            "email": self.email,
            "password": self.password
        }
        result = db.users.insert_one(user_data)
        return result.inserted_id  
    
    #retrieve a user from the database by email
    @staticmethod
    def find_by_email(db, email):
        return db.users.find_one({"email": email})