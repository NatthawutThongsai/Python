l = [1,True,"test"]
for i in l:
    print(i)
l2 = [i for i in range(10)]
print(l2[2:-3])
l2.append("xxx")
print(l2)
l2.insert(0,"yyy")
print(l2)