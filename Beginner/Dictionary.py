#dictionary => key , value
colors = {"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว"}
print(colors["red"])
#create by constructor
animal = dict(cat="แมว")
print(animal["cat"])
print(animal.get("cat"))
#edit data
colors["red"] = "แดง"
#add new member
colors.update({"blue":"สีน้ำเงิน"})
colors["purple"] = "สีม่วง"
print(colors)
for k,v in colors.items():
    print("key = ",k ,"value = ",v)
colors.pop("red")
x = colors.copy()
colors.popitem() #delete latest member
colors.clear() #clear all member
del colors #clear colors from memory
#nested dictionary
market= {
    "xxx":{
        "name":"xx",
        "menu":["x1","x2"]
    },
    "yyy":{
        "name":"yy",
        "menu":["y1","y2"]
    },
    "zzz":{
        "name":"zz",
        "menu":["z1","z2"]
    }
}
print(market["xxx"]["menu"][0])