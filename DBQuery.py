from ShoesDB import app,db,Product

with app.app_context():
    data = db.session.execute(db.select(Product).filter_by(username="helloo"))
    S = Product.query.all()
    for usr in S:
        print(f"Hey {usr.username}")