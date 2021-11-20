from flask import Flask, app, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api, fields, Resource



# app

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseDog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# banco

databaseDog = SQLAlchemy(app)
ma = Marshmallow(app)


# api

api = Api()


# inicialização

api.init_app(app)


# dados do databaseDog

class Dog(databaseDog.Model):
    id_dog = databaseDog.Column(databaseDog.Integer, primary_key=True, autoincrement=True)
    nome = databaseDog.Column(databaseDog.String)
    filme = databaseDog.Column(databaseDog.String)
    ano = databaseDog.Column(databaseDog.String)
    raça = databaseDog.Column(databaseDog.String)


class DogSchema(ma.Schema):
    class Meta:
        fields = (
            'id_dog',
            'nome',
            'filme',
            'ano',
            'raça'
        )

dog_schema = DogSchema()
dogs_schema = DogSchema(many=True)

# informações do Swagger: padrão


# modelo

modelo = api.model('Dog', {
    'nome': fields.String('Digite o nome'),
    'filme': fields.String('Digite o filme'),
    'ano': fields.String('Digite o ano'),
    'raça': fields.String('Digite a raça')
})



# Rotas (CRUD)

# Listar - GET

@api.route('/listar')
class Listar_Todos(Resource):
    def get(self):
        return jsonify(dogs_schema.dump(Dog.query.all()))


# Listar - GET{id_dog}

@api.route('/listar/<int:id_dog>')
class Listar_por_id(Resource):
    def get(self, id_dog):
        return jsonify(dog_schema.dump(Dog.query.get(id_dog)))


# Criar - POST

@api.route('/criar')
class Cadastrar(Resource):
    @api.expect(modelo)
    def post(self):
        dog = Dog(
            nome = request.json['nome'],
            filme = request.json['filme'],
            ano = request.json['ano'],
            raça = request.json['raça']
        )

        databaseDog.session.add(dog)
        databaseDog.session.commit()

        return {
            'mensagem': f'Cachorro com id: {dog.id_dog} cadastrado com sucesso.'
        }
    

# Atualizar - PUT{id}

@api.route('/atualizar/<int:id_dog>')
class Atualizar_por_id(Resource):
    @api.expect(modelo)
    def put(self, id_dog):
        dog = Dog.query.get(id_dog)

        if dog:
            dog.nome = request.json['nome']
            dog.filme = request.json['filme']
            dog.ano = request.json['ano']
            dog.raça = request.json['raça']

            databaseDog.session.commit()

            return {
                'mensagem': f'Cachorro com id: {id_dog} atualizado com sucesso.'
            }
        else:
            return {
                'mensagem': f'Cachorro com id: {id_dog} não foi encontrado.'
            }


# deletar - DELETE{id}

@api.route('/deletar/<int:id_dog>')
class Deletar_por_id(Resource):
    def delete(self, id_dog):
        dog = Dog.query.get(id_dog)

        if dog:
            databaseDog.session.delete(dog)
            databaseDog.session.commit()

            return {
                'mensagem': f'Cachorro com id: {id_dog} deletado com sucesso.'
            }
        else:
            return {
                'mensagem': f'Cachorro com id: {id_dog} não foi encontrado.'
            }
