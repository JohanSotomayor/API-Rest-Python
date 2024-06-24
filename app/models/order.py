from . import db

class Order(db.Model):
    __tablename__ = 'Orders'

    OrderID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Consecutive = db.Column(db.Integer, nullable=False, unique=True)
    OrderDate = db.Column(db.DateTime)
    ClientID = db.Column(db.Integer, db.ForeignKey('Clients.ClientID'))
    TotalAmount = db.Column(db.DECIMAL(precision=18, scale=2))

    def __repr__(self):
        return f"<Order(OrderID={self.OrderID}, Consecutive={self.Consecutive}, OrderDate={self.OrderDate}, ClientID={self.ClientID}, TotalAmount={self.TotalAmount})>"
