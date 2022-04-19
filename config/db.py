from pymongo import MongoClient
from decouple import config

conn_str = config("connectionString")

conn = MongoClient(conn_str)