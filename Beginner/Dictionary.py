#dictionary => key , value
colors = {"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว"}
print(colors["red"])
#create by constructor
animal = dict(cat="แมว")
print(animal["cat"])
print(animal.get("cat"))
#edit data
colors["red"] = "แดง"
print(colors)