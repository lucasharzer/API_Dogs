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
 
 - Models
 
 <span>
      <img src="https://user-images.githubusercontent.com/85804895/142741708-fc600f15-fd9e-4a12-9f8d-70c6116c0d92.gif" width=900>
</span>

- Routes

 <span>
      <img src="https://user-images.githubusercontent.com/85804895/142741734-1b44e4d9-a9ef-4710-8122-000883c4aee4.gif" width=900>
</span>

- Create

 <span>
      <img src="https://user-images.githubusercontent.com/85804895/142741822-40f31cc2-b9f2-4467-86c4-e4597a6f9104.gif" width=900>
</span>

- Read

 <span>
      <img src="https://user-images.githubusercontent.com/85804895/142741851-4e684295-f3c7-45d6-bd38-502e1de53377.gif" width=900>
</span>

- Read{id}

 <span>
      <img src="https://user-images.githubusercontent.com/85804895/142741870-b3b5f8ca-3c68-443c-998d-a37a613eac9c.gif" width=900>
</span>

- Update{id}

 <span>
      <img src="https://user-images.githubusercontent.com/85804895/142741901-a12bd05f-4c26-4725-afd6-39054cf9d5ca.gif" width=900>
</span>

- Delete{id}

 <span>
      <img src="https://user-images.githubusercontent.com/85804895/142741927-0450bf2f-8a51-4076-8388-7ebe3fd358cc.gif" width=900>
</span>


