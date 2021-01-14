#create function
y=10 #global variable
'''
argrument => variable that push into function
parameter => value that recieve from argrument
'''
def fibonacci(x):
    y =15 #local variable
    if x<2:
        return x
    return fibonacci(x-1)+fibonacci(x-2)
while True:
    z=int(input())
    print(fibonacci(z))
    if z<0:
        break
# *args
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(1,2,3,4,5,6,7,8,9,10))
def addnumber(number):
    if number==5:
        return
    number+=1
    print(number)
    addnumber(number)
def summation(number):
    if number==1:
        return 1
    return summation(number-1) + number
addnumber(0)
print(summation(10))
def factorial(number):
    if number==1:
        return 1
    return factorial(number-1) * number
print(factorial(5))
#lambda function
s=lambda name:name
sum= lambda x,y: x+y
print(s("xxx"))
print(sum(5,10))
