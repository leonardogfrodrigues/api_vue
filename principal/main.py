

from email.policy import HTTP
from genericpath import exists
from itertools import count
from queue import Empty
from flask import Flask, request, jsonify #Importando a biblioteca Flask
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request #Biblioteca para endpoints
from pydantic import BaseModel
from typing import Optional, Dict, Any
#from http import server
from tinydb import TinyDB, Query
from flask_cors import CORS



import logging
import unittest

server = Flask("Cadastro_Opss") #Criando aplicação
CORS(server)

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://127.0.0.1:5000/',
            'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE'
        },
        'body': json.dumps('Hello from Lambda!')
    }

spec = FlaskPydanticSpec('flask', title= 'Endpoints')
spec.register(server)

database = TinyDB('database.json')



class Cliente(BaseModel):
    nome: str
    email: str
    telefone: Optional[int]
    endereco: str
    profissao: str
    curriculo: str
   
class Clientes(BaseModel):
    #clientes: list[Cliente]
    count: int

@server.get("/clientes") #Estabelecendo a rota do servidor com o metodo GET
@spec.validate(resp=Response(HTTP_200=Clientes))
def buscar_Clientes():
    return jsonify(
        Clientes(
            clientes=database.all(),
            count=len(database.all())
            ).dict()
    )
   # return jsonify(database.all())

@server.post("/clientes") #Estabelecendo a rota do servidor com o metodo POST
@spec.validate(body=Request(Cliente), resp=Response(HTTP_200=Cliente))
def publicar_Clientes():
  """Cadastrando um cliente"""  
  body = request.context.body.dict() #Dados em json convertidos para um dict em python
  database.insert(body)
  if body is not request.context.body.dict():
        logging.basicConfig(  #Log para a funcao main se ela estiver certa
        level= logging.ERROR,
        format= '%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='LOG_api.log',
        filemode='w'
    )
  
  return body

@server.put('/clientes/<int:telefone>') #Estabelecendo a rota do servidor com o metodo PUT
@spec.validate(body=Request(Cliente), resp=Response(HTTP_200=Cliente))
def atualizar_Clientes(telefone):
    Cliente = Query()
    body = request.context.body.dict()
    
    if Cliente.telefone != telefone:
        logging.basicConfig(
        level= logging.INFO,
        format= '%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='LOG.log',
        filemode='w'    
    )
        logging.INFO('Cliente nao encontrado, digite o numero correto de telefone')
    
    database.update(body, Cliente.telefone == telefone)
    return jsonify(body)

@server.delete('/clientes/<int:telefone>') #Estabelecendo a rota do servidor com o metodo DELETE
@spec.validate(resp=Response('HTTP_204'))
def deletar_Clientes(telefone):
    Cliente = Query()
    
    if count==0:
        logging.basicConfig(
        level= logging.WARNING,
        format= '%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='LOG2.log',
        filemode='w'    
    )
        logging.INFO('BD esta vazio, nao foi possivel deletar')
       
    database.remove(Cliente.telefone == telefone)
    return jsonify({})


if __name__ == '__main__':
    logging.basicConfig(  #Log para a funcao main se ela estiver certa
        level= logging.DEBUG,
        format= '%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='LOG.log',
        filemode='w'
)
else:
    logging.basicConfig(
        level= logging.CRITICAL, #Log para a funcao main se ela estiver errada
        format= '%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='LOG.log',
        filemode='w'
)

server.run()
unittest.main() 