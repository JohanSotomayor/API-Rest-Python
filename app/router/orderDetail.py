# app/views.py
from flask import Blueprint, jsonify, request, g
from sqlalchemy.exc import SQLAlchemyError
from ..models import db, OrderDetail, Order, Client, Product

class OrderDetailRoutes:
    def __init__(self):
        self.main = Blueprint('orderDetailDetails', __name__, url_prefix='/api/orderDetails')
        self.OrderDetail_routes()

    def OrderDetail_routes(self):
        @self.main.route('/', methods=['POST'])
        def create_orderDetail():
            try :
                data = request.get_json()
                list_orders = []
                print('lista ', data)

                if not isinstance(data, list):
                    return jsonify({'error': 'Los datos deben ser una lista de registros'}), 400


                for orderDetail in data:
                    new_orderDetail = OrderDetail(
                        OrderID = orderDetail['orderID'],
                        ProductID = orderDetail['productID'],
                        Quantity = orderDetail['quantity'],
                        UnitPrice = orderDetail['unitPrice'],
                        AmountIva = orderDetail.get('amountIva'),
                    ) 
                    list_orders.append(new_orderDetail)
               
                db.session.add_all(list_orders)
                db.session.commit()
                
                return jsonify({'data':True, 'message': 'Detalles de venta creada existosamente'}), 201
                
            except SQLAlchemyError as e:
                print(e)
                db.session.rollback() 
                return jsonify({'message': e}), 500 

        @self.main.route('/<int:id>', methods=['GET'])

        def get_orderDetails(id):
    
            orderId = id
            query_result = db.session.query(Order, OrderDetail, Client, Product)\
            .join(OrderDetail, Order.OrderID == OrderDetail.OrderID)\
            .join(Client, Order.ClientID == Client.ClientID)\
            .join(Product, OrderDetail.ProductID == Product.ProductID)\
            .filter(Order.OrderID == orderId).all()
            print('query_result',query_result)

            orders = {}
            for order, orderDetail, client, product in query_result:
                if order.OrderID not in orders:
                    orders[order.OrderID] = {
                            'consecutive': order.Consecutive,
                            'orderDate': order.OrderDate,
                            'totalAmount': order.TotalAmount,
                            'clientID': client.ClientID,
                            'clientName': client.Name,
                            'clientCardId': client.CardId,
                            'orderDetails': []
            
                        } 
                
                orders[order.OrderID]['orderDetails'].append({
                        'quantity' : orderDetail.Quantity,
                        'unitPrice' : orderDetail.UnitPrice,
                        'quantity' : orderDetail.Quantity,
                        'AmountIva' : orderDetail.AmountIva,
                        'productName': product.Name,
                        'productPrice': product.Price,
                        'productCode': product.Code,
                        'productPercentIva': product.PercentIva,
                })

                
            return jsonify({"data":orders[order.OrderID]}), 200

        @self.main.route('/', methods=['DELETE'])
        def delete_orderDetail():
            try :
                ids = request.args.getlist('ids') 
                list_ids = [int(num) for num in ids[0].split(',')]
                products = OrderDetail.query.filter(OrderDetail.OrderDetailID.in_(list_ids)).all()
                for product in products:
                    db.session.delete(product) 
                db.session.commit()
                return jsonify({'message': 'Products deleted successfully'}), 200
            except SQLAlchemyError as e:
                db.session.rollback() 
                return jsonify({'message': 'Error en la base de datos'}), 500 
