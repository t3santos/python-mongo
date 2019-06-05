from pymongo import MongoClient
from lib import DadosAbertos

server_mongo = 'localhost'

# Conexao ao mongoDB
conn = MongoClient(server_mongo, 27017)

while True:

  # Conexao ao database
  banco = conn['projetoDep']

  # Conexao a tabela de banco de dados
  table = banco['deputados']

  # Array que vai receber os dados do deputados
  list_deputados = []

  #Conexao com api dos dados publicos
  obj = DadosAbertos()

  # Listando os deputados
  list_dep = obj.deputados()

  for dep in list_dep:
      info = {
             '_id': dep['id'],
             'Nome': dep['nome'],
             'Partido': dep['siglaPartido'],
             'Foto': dep['urlFoto']
      }
      list_deputados.append(info)


  # Inserindo dados no mongodb
  retorno = table.insert_many(list_deputados)

  #Imprindo o retorno de ids
  print(retorno.inserted_ids)