import pickle

with open("ShoesData","rb") as f:
    data = pickle.load(f)

l = len(data['Name'])
cat=[]
sub=[]
aPrice=""
for i in range(5):
    if data["Price"][i] is not None :
        bPrice = data["Price"][i].strip()

        if not bPrice[0].isnumeric():
            aPrice = int(bPrice[1:].replace(',',''))
            print(f"{bPrice} :-> {aPrice}")

        else:
            aPrice = bPrice
        print(f"{bPrice} :-> {aPrice}")
        # print("\n")
    sp=''
    for s in data["Specification"][i]:
        sp = sp+s
    print(sp)
print(l)
print(len(set(data["Link"])))
