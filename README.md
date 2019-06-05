# Desenvolvimento o BackEnd

Para o desenvolvimento localmente vamos inicializar o MongoDB localmente.

Iniciando o MongoDB:

```
$ docker run -d -p 27017-27019:27017-27019  --name mongodb mongo:latest
```


Criando a imagem:

Antes de criar a imagem Docker, 


```
$ pip freeze  >> requirements
```

Criando a imagem Docker:

```
$  docker build -t clodonil/app-back:latest .
```

```
$ docker build -t  clodonil/app-front:latest .
```


Referência:

- [MongoDB](https://medium.com/grupy-rn/trabalhando-com-python-e-mongodb-1d23ee042658)
- [CreateTable](https://www.w3schools.com/python/python_mongodb_create_db.asp)
- [Insert](https://www.w3schools.com/python/python_mongodb_insert.asp)
