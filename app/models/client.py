
from . import db

class Client(db.Model):
    __tablename__ = 'Clients'
    ClientID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CardId = db.Column(db.String(20), unique=True, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Address = db.Column(db.String(255))
    Phone = db.Column(db.String(20))
    Email = db.Column(db.String(100), nullable=False)

    def __init__(self, CardId, Name, Address=None, Phone=None, Email=None):
        self.CardId = CardId
        self.Name = Name
        self.Address = Address
        self.Phone = Phone
        self.Email = Email

    def __repr__(self):
        return f"<Product(name='{self.Name}', Address='{self.Address}', CardId='{self.CardId}')>"
