from ShoesDB import app,db,Shoes

with app.app_context():
    data = db.session.execute(db.select(Shoes).filter_by(username="helloo"))
    S = Shoes.query.all()
    for usr in S:
        print(f"Hey {usr.username}")