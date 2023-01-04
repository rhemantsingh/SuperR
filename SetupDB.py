from ShoesDB import app, db,Logins,Product
import pickle


with app.app_context():
    # db.drop_all()
    # db.create_all()
    #
    # with open('ShoesData','rb') as f:
    #     data = pickle.load(f)
    #
    # for i in range(4):
    #     if data['Name'][i] !="None" and data['Link'][i] != "None" and data["Image"][i] != "None" and data["Price"][i] != "None":
    #         aprice=0
    #         if data["Price"][i] is not None:
    #             bPrice = data["Price"][i].strip()
    #
    #             if not bPrice[0].isnumeric():
    #                 aPrice = bPrice[1:]
    #             else:
    #                 aPrice = bPrice
    #             aPrice = int(aPrice.replace(',',''))
    #         mprice = 0
    #         if data["MRP"][i] is not None or data["MRP"][i] != "None":
    #             rPrice = data["MRP"][i].strip()
    #
    #             if not rPrice[0].isnumeric():
    #                 mPrice = rPrice[1:]
    #             else:
    #                 mPrice = rPrice
    #             print(mPrice)
    #             mPrice = int(float(mPrice.replace(',', '')))
    #         sp=''
    #         for s in data["Specification"][i]:
    #             sp = sp + s
    #         try:
    #             prod1 = Product(name=data['Name'][i], link=data['Link'][i], image=data['Image'][i],
    #                         price=aPrice, mrp=mPrice, color=data['Color'][i], specification=sp, category=data['Category'][i], subCategory=data['Subcategory'][i])
    #             db.session.add(prod1)
    #             db.session.commit()
    #         except:
    #
    #             print("Error to hai")

    # l = db.session.execute(db.select(Product))
    l1 = Product.query.all()

    for log in l1:
        print(log)
