import sys
from pymongo import MongoClient

conn = MongoClient("mongodb+srv://biuser:<password>@claus-mongo-cluster.2skj4.azure.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")