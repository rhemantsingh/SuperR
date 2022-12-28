from ShoesDB import app, db,Logins,Laptop

with app.app_context():
    db.create_all()

    # admin=Shoes(username="helloo", password="niihaaoo")
    # guest=Shoes(username="wow",password="mom")
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.add(Laptop(name="Acer aspire 5"))
    #db.session.commit()
