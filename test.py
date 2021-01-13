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