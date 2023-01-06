from ShoesDB import app, db,Logins,Product
import pickle


def clear_Color(color):
    if color[0].isnumeric():
        color = color[1:]
    return color

def clear_Price(rs):
    rs = rs.strip()
    rs = rs.replace(',', '')
    if not rs[0].isnumeric():
        try:
            rs = float(rs[1:])
        except:
            rs = rs[1:]
    return rs

with app.app_context():
    # db.drop_all()
    # db.create_all()
    #
    # with open('ShoesData','rb') as f:
    #     data = pickle.load(f)
    #
    # for i in range(len(data['Name'])):
    #     if data['Name'][i] !="None" and data['Link'][i] != "None" and data["Image"][i] != "None" and data["Price"][i] != "None":
    #         colour = clear_Color(data["Color"][i])
    #         aPrice = data["Price"][i]
    #         if aPrice != "None" and aPrice != None:
    #             aPrice = clear_Price(aPrice)
    #         else:
    #             aPrice= "None"
    #         mPrice = data["MRP"][i]
    #         if mPrice != "None" and mPrice != None:
    #             mPrice = clear_Price(mPrice)
    #         else:
    #             mPrice = "None"
    #         sp = ''
    #         for s in data["Specification"][i]:
    #             sp = sp + "%%" + s
    #         try:
    #             prod1 = Product(name=data['Name'][i], link=data['Link'][i], image=data['Image'][i],
    #                         price=aPrice, mrp=mPrice, color=colour, specification=sp,
    #                             category=data['Category'][i], subCategory=data['Subcategory'][i])
    #             db.session.add(prod1)
    #             db.session.commit()
    #         except:
    #             print('error to hai')
    #             print(data['Link'][i])
    #     print(i)
    products = Product.query.all()
    print(len(products))
    _list = []
    double = []
    for pro in products:
        if pro.link not in _list:
            _list.append(pro.link)
        else:
            double.append(pro.link)
    print(len(_list))
    print(len(double))

