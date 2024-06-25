from .error import ErrorRoutes
from .products import ProductRoutes
from .clients import ClientsRoutes
from .order import OrderRoutes
from .orderDetail import OrderDetailRoutes

class RouterConfig:

    @staticmethod
    def register_blueprints(app):
        error_routes = ErrorRoutes()
        product_routes = ProductRoutes()
        clients_routes = ClientsRoutes()
        Order_routes = OrderRoutes()
        OrderDetail_routes = OrderDetailRoutes()
        app.register_blueprint(error_routes.main)
        app.register_blueprint(product_routes.main)
        app.register_blueprint(clients_routes.main)
        app.register_blueprint(Order_routes.main)
        app.register_blueprint(OrderDetail_routes.main)

        
