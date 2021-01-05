l = [1,True,"test"]
for item in l:
    print(item)
l2 = [i for i in range(10)]
print(l2[2:-3])
l2.append("xxx")
l2.insert(0,"yyy")
l2.remove("xxx")
l2.pop()
del l2[1]
print(l2)
del l #remove from memory
l2.clear() #delete the member of list
l = [i for i in range(3)]
l2 = l.copy()
l3 = ["a","b","c"]
print(l2+l3)