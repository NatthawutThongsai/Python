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

li1 = ["a","b","c"]
li2 = ["x","y","z"]
for j,k in zip(li1,li2):
    print(j+k)
l.sort()
l.reverse()
l2.extend(li2)
print(l2)
print(l2[::-1])
print(l)