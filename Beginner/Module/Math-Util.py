x = min(3,4,5)
y = max(3,4,5)
ab = abs(-50)
po = pow(5,3)
import math
result = math.sqrt(64)
#ceil floor log sin
import random
r1 = random.random()
r2 = random.uniform(5,10)
r3 = random.randrange(1,10)
r4 = random.randrange(1,10,3)
r5 = random.randint(4,10)
l = [3,14,4,"a",True,1.27]
for i in range(5):
    #print("random.choice ",i," ",random.choice(l))
    random.shuffle(l) #shuffle in list
#crack password
pw = "3564"
while True:
    st = ""
    for i in range(len(pw)):
        r = random.randint(1,10)
        st = st+str(r)
        print(st)
    if st==pw:
        print("Complete")
        break