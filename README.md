# Descrição

Rest API de cachorros com python, flask, flask-sqlalchemy (banco de dados), flask-marshmallow, marshmallow-sqlalchemy e flask-restx aplicada no Swagger. Nessa API, um cachorro tem os seguintes dados (id_dog, nome, filme, ano e raça) e é possível: Listar todos os cachorros ( GET ), listar cachorros por id ( GET{id} ), deletar cachorros por id ( DELETE{id} ), atualizar cachorros por id ( PUT{id} ) e cadastrar cachorros inserindo todos os dados ( POST ).

Obs: o arquivo requirements.txt possui todos os pacotes e suas respectivas versões usadas para executar a API.

# Comandos no terminal para configuração

- Instalar os pacotes: 

```bash
python setup.py develop
```
- Configurar o app:

Para Windows:
```bash
set FLASK_APP=app.py 
```
```bash
set FLASK_DEBUG=True
```
Para Linux:
```bash
export FLASK_APP=app.py
```
```bash
export FLASK_DEBUG=True
```

- Criar o banco de dados:
 ```bash
 python
 ```
  ```bash
 from appDog import databaseDog
 ```
  ```bash
 databaseDog.create_all()
 ```
  ```bash
 exit()
 ```
 
 # Rodando a aplicação
  ```bash
 flask run
 ```
 # Resultado no Swagger

 http://localhost:5000
