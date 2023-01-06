import pickle

with open("ShoesData", "rb") as f:
    data = pickle.load(f)

l = len(data['Name'])
cat=[]
sub=[]
aPrice=""
for i in range(l):
    # if data["Price"][i] is not None :
    #     bPrice = data["Price"][i].strip()
    #
    #     if not bPrice[0].isnumeric():
    #         aPrice = int(bPrice[1:].replace(',',''))
    #         print(f"{bPrice} :-> {aPrice}")
    #
    #     else:
    #         aPrice = bPrice
    #     print(f"{bPrice} :-> {aPrice}")
    #     # print("\n")
    # sp=''
    # for s in data["Specification"][i]:
    #     sp = sp+s
    # print(sp)
    if data["Color"][i][0].isnumeric():
        data["Color"][i]=data["Color"][i][1:]
    print(data["Color"][i])
print(l)

