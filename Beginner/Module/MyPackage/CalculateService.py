PI = 3.14
ROOT = 1.414
def subtraction(num1,num2):
    print("Subtraction = ",(num1-num2))
def addition(*args):
    total = 0
    for item in args:
        total+=item
    print("Summation = ",total)
def power(num1,m):
    print(num1**m)