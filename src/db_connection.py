import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

""" Get mongoDB URI from environment variable """
MONGODB_URI = os.environ.get('MONGODB_URI')

""" Connect to mongoDB """
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

""" Try sending a request to the server """
try:
  client.server_info()
  print('Connection successful')
except Exception as e:
  print(f'Error: {e}')

""" get the database """
db = client.get_database("HIS")