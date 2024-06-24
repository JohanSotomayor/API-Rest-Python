from . import db

class Category(db.Model):
    __tablename__ = 'Categories'

    CategoryID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CategoryName = db.Column(db.String(100), nullable=False)
     # Establece la relación con la tabla Products
    products = db.relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(CategoryID={self.CategoryID}, CategoryName='{self.CategoryName}')>"
