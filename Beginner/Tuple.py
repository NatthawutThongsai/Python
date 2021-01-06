tup = (1,"a",True,1.2) #ใส่ค่าได้ทุกtype
lis = list(tup)
lis[0] = 2 #change member of tuple by cast to list
tup = tuple(lis) #cast list back to tuple
c = tup.count("a") #count member in tuple
ind = tup.index("a") #find index of member
new= ("new",) # tuple can add member only same type(tuple)
print(tup+new+tuple(("new2",)))
a,b,c,d = tup
print(a,b,c,d)
x =(50,60)
y =(88,99)
x,y = y,x
print(x,y)
character = ("k",'n',"o","t")
name = "".join(character)
print(name)
#tuple cannot sort must change to list and sort

