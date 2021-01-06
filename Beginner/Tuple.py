tup = (1,"a",True,1.2) #ใส่ค่าได้ทุกtype
lis = list(tup)
lis[0] = 2
tup = tuple(lis)
print(tup)