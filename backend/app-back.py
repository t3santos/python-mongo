from pymongo import MongoClient
from lib import DadosAbertos
import schedule
import time
import os

def coletor():

   # Check se a variavel de ambiente do mongodb foi declarado
   if not 'MONGODB' in os.environ:
       print('Set a variavel MONGODB')
       break

   # hostname do mongodb, consultado via variavel de ambiente
   server_mongo = os.environ['MONGODB']

   # Conexao ao mongoDB
   conn = MongoClient(server_mongo, 27017)


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
             '_id'    : dep['id'],
             'Nome'   : dep['nome'],
             'Partido': dep['siglaPartido'],
             'Foto'   : dep['urlFoto']
      }
      list_deputados.append(info)


   # Inserindo dados no mongodb
   retorno = table.insert_many(list_deputados)


#Criando o schedule
schedule.every().day.at("10:30").do(job)

while True:
   schedule.run_pending()
   time.sleep(1)
