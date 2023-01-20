from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv("db")

client = MongoClient(connection_string)


