tup = (1,"a",True,1.2) #ใส่ค่าได้ทุกtype
lis = list(tup)
lis[0] = 2 #change member of tuple by cast to list
tup = tuple(lis)
new= ("new",) # tuple can add member only same type(tuple)
print(tup+new+tuple(("new2",)))
