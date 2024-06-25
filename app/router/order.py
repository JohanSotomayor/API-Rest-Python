# app/views.py
from flask import Blueprint, jsonify, request, g
from sqlalchemy.exc import SQLAlchemyError
from ..models import db, Order, Client, OrderDetail

class OrderRoutes:
    def __init__(self):
        self.main = Blueprint('orders', __name__, url_prefix='/api/orders')
        self.Order_routes()

    def Order_routes(self):
        @self.main.route('/', methods=['POST'])
        def create_order():
            try :
                data = request.get_json()
                new_order = Order(
                    Consecutive = data['consecutive'],
                    OrderDate = data['orderDate'],
                    ClientID = data['clientID'],
                    TotalAmount = data['totalAmount'],
                )
                order_exist =  Order.query.filter_by(Consecutive=data['consecutive']).first()
                if order_exist:
                    return jsonify({'message': 'Consecutivo de orden ya existe'}), 409
                else:
                    db.session.add(new_order)
                    db.session.commit()
                    print('new_order', new_order)
                    data['orderID']= new_order.OrderID
                    print('data', data)
                    return jsonify({'data':data, 'message': 'Orden de venta creada existosamente'}), 201
                
            except SQLAlchemyError as e:
                print(e)
                db.session.rollback() 
                return jsonify({'message': e}), 500 

        @self.main.route('/', methods=['GET'])
        def get_orders():
            query_result = db.session.query(Order, Client).join(Client, Order.ClientID == Client.ClientID).all()
            result = [
                {
                    'orderID' : order.OrderID,
                    'consecutive' : order.Consecutive,
                    'orderDate' : order.OrderDate,
                    'clientID' : order.ClientID,
                    'totalAmount' : order.TotalAmount,
                    'clientID': client.ClientID,
                    'clientName': client.Name,
                    'clientCardId': client.CardId,
                    
                } for order, client in query_result
            ]
            return jsonify({"data":result}), 200
        
        @self.main.route('/dates/', methods=['GET'])
        def get_ordersDate():
            try :
                date = request.args.get('date')
                print('date', date)
                query_result = db.session.query(Order, Client).join(Client, Order.ClientID == Client.ClientID)\
                    .filter(Order.OrderDate >= date).all()
                result = [
                    {
                        'orderID' : order.OrderID,
                        'consecutive' : order.Consecutive,
                        'orderDate' : order.OrderDate,
                        'clientID' : order.ClientID,
                        'totalAmount' : order.TotalAmount,
                        'clientID': client.ClientID,
                        'clientName': client.Name,
                        'clientCardId': client.CardId,

                    } for order, client in query_result
                ]
                return jsonify({"data":result}), 200
            except SQLAlchemyError as e:
                print(e)
                db.session.rollback() 
                return jsonify({'message': 'Error en la base de datos'}), 500 


        @self.main.route('/', methods=['DELETE'])
        def delete_order():
            try :
                ids = request.args.getlist('ids') 
                list_ids = [int(num) for num in ids[0].split(',')]

                # Eliminamos referencia en Order Details
                ordersDetails = OrderDetail.query.filter(OrderDetail.OrderID.in_(list_ids)).all()
                for orderD in ordersDetails:
                    db.session.delete(orderD) 
                db.session.commit()

                orders = Order.query.filter(Order.OrderID.in_(list_ids)).all()
                for order in orders:
                    db.session.delete(order) 
                db.session.commit()
                return jsonify({'message': 'orders deleted successfully'}), 200
            
            except SQLAlchemyError as e:
                print(e)
                db.session.rollback() 
                return jsonify({'message': 'Error en la base de datos'}), 500 
