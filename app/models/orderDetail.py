from . import db

class OrderDetail(db.Model):
    __tablename__ = 'OrderDetails'

    OrderDetailID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrderID = db.Column(db.Integer, db.ForeignKey('Orders.OrderID'))
    ProductID = db.Column(db.Integer, db.ForeignKey('Products.ProductID'))
    Quantity = db.Column(db.Integer)
    UnitPrice = db.Column(db.DECIMAL(precision=18, scale=2))
    AmountIva = db.Column(db.DECIMAL(precision=10, scale=2))

    def __repr__(self):
        return f"<OrderDetail(OrderDetailID={self.OrderDetailID}, OrderID={self.OrderID}, ProductID={self.ProductID}, Quantity={self.Quantity}, UnitPrice={self.UnitPrice}, AmountIva={self.AmountIva})>"
