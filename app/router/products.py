# app/views.py
from flask import Blueprint, jsonify, g
# from models import Product

class ProductRoutes:
    def __init__(self):
        self.main = Blueprint('main', __name__)
        self.register_routes()

    def register_routes(self):
        @self.main.route('/products')
        def get_products():
            # products = g.session.query(Product).all()
            # return jsonify([str(product) for product in products])
            return

# def register_blueprints(app):
#     product_routes = ProductRoutes()
#     app.register_blueprint(product_routes.main)
