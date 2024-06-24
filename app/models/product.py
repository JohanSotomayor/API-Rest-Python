from sqlalchemy.orm import relationship
from . import db

class Product(db.Model):
    __tablename__ = 'Products'

    ProductID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.String(500))
    Code = db.Column(db.String(20), nullable=False, unique=True)
    Price = db.Column(db.DECIMAL(precision=10, scale=2), nullable=False)
    Stock = db.Column(db.Integer, nullable=False)
    HasIva = db.Column(db.Boolean, nullable=False, default=False)
    PercentIva = db.Column(db.Float)
    CategoryID = db.Column(db.Integer, db.ForeignKey('Categories.CategoryID'))
    
    # Relación con la tabla Categories
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(Name='{self.Name}', Price={self.Price}, Stock={self.Stock})>"