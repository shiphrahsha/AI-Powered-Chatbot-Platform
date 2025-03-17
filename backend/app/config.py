from dotenv import load_dotenv
import os

load_dotenv()

#get the mongoURL and secretKey
class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")