# app/views.py
from flask import Blueprint, jsonify, request, g
from sqlalchemy.exc import SQLAlchemyError
from ..models import db, Product
# from models import Product

class ProductRoutes:
    def __init__(self):
        self.main = Blueprint('products', __name__, url_prefix='/api/products')
        self.Products_routes()

    def Products_routes(self):
        @self.main.route('/', methods=['POST'])
        def create_product():
            try :
                data = request.get_json()
                new_product = Product(
                    Name = data['name'],
                    Description = data.get('description'),
                    Code = data['code'],
                    Price = data['price'],
                    Stock = data['stock'],
                    HasIva = data['hasIva'],
                    PercentIva = data.get('percentIva'),
                    CategoryID = data['categoryID'],
                )
                product_exist =  Product.query.filter_by(Code=data['code']).first()
                if product_exist:
                    return jsonify({'message': 'Codigo de producto ya existe'}), 409
                else:
                    db.session.add(new_product)
                    db.session.commit()
                    print('new_product', new_product)
                    data['productID']= new_product.ProductID
                    print('data', data)
                    return jsonify({'data':data, 'message': 'Producto creado existosamente'}), 201
                
            except SQLAlchemyError as e:
                print(e)
                db.session.rollback() 
                return jsonify({'message': e}), 500 

        @self.main.route('/', methods=['GET'])
        def get_products():
            products = Product.query.all()
            result = [
                {
                    'productID': product.ProductID,
                    'name': product.Name,
                    'description': product.Description,
                    'code': product.Code,
                    'price': product.Price,
                    'stock': product.Stock,
                    'hasIva': product.HasIva,
                    'percentIva': product.PercentIva,
                    'categoryID': product.CategoryID,
                } for product in products
            ]
            return jsonify({"data":result}), 200

        @self.main.route('/', methods=['DELETE'])
        def delete_product():
            try :
                ids = request.args.getlist('ids') 
                list_ids = [int(num) for num in ids[0].split(',')]
                products = Product.query.filter(Product.ProductID.in_(list_ids)).all()
                for product in products:
                    db.session.delete(product) 
                db.session.commit()
                return jsonify({'message': 'Products deleted successfully'}), 200
            except SQLAlchemyError as e:
                db.session.rollback() 
                return jsonify({'message': 'Error en la base de datos'}), 500 
