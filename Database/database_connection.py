from pymongo import MongoClient
from Database.school_database_variables import *

client = MongoClient(localhost)
db = client[school_database]

