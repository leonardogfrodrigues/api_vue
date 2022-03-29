from http import server
from typing import Collection
from pymongo import MongoClient
from flask_mongoengine import MongoEngine

uri = 'mongodb://root:Cadastro@localhost:27017/'


DB_URI = "mongodb+srv://leonardogfrodrigues:<cadastro>@cluster0.pybs9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format
(mongodb_password, database_name)
server.config["MONGODB_HOST"]= DB_URI
db = MongoEngine()
db.init_server(server)

#db = MongoClient(uri)
#database = client['Cadastro']
#collection = database['Clientes']
