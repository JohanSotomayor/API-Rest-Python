# Crear un nuevo cliente

from flask import Blueprint, jsonify, request, g
from sqlalchemy.exc import SQLAlchemyError
from ..models import db, Client

class ClientsRoutes:
    def __init__(self):
        self.main = Blueprint('clients', __name__, url_prefix='/api/clients')
        self.Clients_routes()

    def Clients_routes(self):
        @self.main.route('', methods=['POST'])
        def create_client():
            try :
                data = request.get_json()
                new_client = Client(
                    CardId=data['cardId'],
                    Name=data['name'],
                    Address=data.get('address'),
                    Phone=data.get('phone'),
                    Email=data['email']
                )
                client_exist =  Client.query.filter_by(CardId=data['cardId']).first()
                if client_exist:
                    return jsonify({'message': 'Cliente con Numero de identificación existente'}), 409
                else:
                    db.session.add(new_client)
                    db.session.commit()
                    print('new_client', new_client)
                    data['clientID']= new_client.ClientID
                    print('data', data)
                    return jsonify({'data':data,'message': 'Cliente creado existosamente'}), 201
                
            except SQLAlchemyError as e:
                print(e)
                db.session.rollback() 
                return jsonify({'message': 'Error en la base de datos'}), 500 

        # Obtener todos los clientes
        @self.main.route('/', methods=['GET'])
        def get_clients():
            clients = Client.query.all()
            result = [
                {
                    'clientID': client.ClientID,
                    'cardId': client.CardId,
                    'name': client.Name,
                    'address': client.Address,
                    'phone': client.Phone,
                    'email': client.Email
                } for client in clients
            ]
            return jsonify({"data":result}), 200

        # Obtener un cliente por ID
        @self.main.route('/<int:id>', methods=['GET'])
        def get_client(id):
            client = Client.query.get_or_404(id)
            result = {
                'ClientID': client.ClientID,
                'CardId': client.CardId,
                'Name': client.Name,
                'Address': client.Address,
                'Phone': client.Phone,
                'Email': client.Email
            }
            return jsonify(result), 200

        # Actualizar un cliente por ID
        @self.main.route('/<int:ids>', methods=['PUT'])
        def update_client(id):
            data = request.get_json()
            client = Client.query.get_or_404(id)
            client.CardId = data.get('CardId', client.CardId)
            client.Name = data.get('Name', client.Name)
            client.Address = data.get('Address', client.Address)
            client.Phone = data.get('Phone', client.Phone)
            client.Email = data.get('Email', client.Email)
            db.session.commit()
            return jsonify({'message': 'Client updated successfully'}), 200

        # Eliminar un cliente por ID
        @self.main.route('/', methods=['DELETE'])
        def delete_client():
            try :
                ids = request.args.getlist('ids') 
                list_ids = [int(num) for num in ids[0].split(',')]
                clients = Client.query.filter(Client.ClientID.in_(list_ids)).all()
                for client in clients:
                    db.session.delete(client) 
                db.session.commit()
                return jsonify({'message': 'Clients deleted successfully'}), 200
            except SQLAlchemyError as e:
                db.session.rollback() 
                return jsonify({'message': 'Error en la base de datos'}), 500 
