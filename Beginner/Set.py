'''
                ข้อมูลต่างtype  แก้ไขสมาชิก   ข้อมูลซ้ำได้
list = []           1           1           1
tuple = ()          1           0           1
set = {}            1           1           0 ลำดับไม่แน่นอน
'''
#สร้าง set
s = {1,2,3}
s.add(4) #addd member to set
l = [5,6,7]
s.update(l) #update set by list
if 5 in s: #check member in set
    print(len(s)) #find set size
s.remove(5) #remove member if dont found -> error
s.discard(8) #remove if dont found -> no error
s.clear() #clear member in s but s is still exist
print(s)
del s #delete var s

"""
operator of set 
"""
#union
s1 = {1,2,3}
s3 = s1.copy() #copy member from s1
s2 = {3,4,5}
sa = s1.union(s2)
s3.update(s2)
print(sa)
del sa
#difference
sa = s1.difference(s2)
print(sa)
del sa
s1.difference_update(s2)
print(s1)
s1 = {1,2,3}
#intersection
sa = s1.intersection(s2)
print(sa)
del sa
#subset & superset
s1 = {1,2,3}
s2 = {1,3}
print("{1,3} is subset {1,2,3} -> ",s2.issubset(s1))
print("{1,3} is superset {1,2,3} -> ",s2.issuperset(s1))
#min & max
print("min & max ",min(s1),max(s2))
