from datetime import datetime
from bson import ObjectId

from datetime import datetime
from bson import ObjectId

class Chat:
    #initialize a Chat instance with user_id, message, response, and timestamp
    def __init__(self, user_id, message, response):
        self.user_id = user_id
        self.message = message
        self.response = response
        self.timestamp = datetime.utcnow()
        
     #save the chat in data to the database
    def save(self, db):
        chat_data = {
            "user_id": self.user_id,
            "message": self.message,
            "response": self.response,
            "timestamp": self.timestamp
        }
        db.chats.insert_one(chat_data)
        
    #retrieve chat history for a given user_id from the database, sorted by timestamp
    @staticmethod
    def find_by_user_id(db, user_id):
        chats = list(db.chats.find({"user_id": user_id}).sort("timestamp", 1))
        # Convert ObjectId to string for each chat
        for chat in chats:
            chat["_id"] = str(chat["_id"])
        return chats