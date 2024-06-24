from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .client import Client
from .category import Category
from .product import Product
from .order import Order
from .orderDetail import OrderDetail



