'''
try:
    num1 = int(input("number 1 = "))
    num2 = int(input("number 2 = "))
    result = num1/num2
    print(result)
except ValueError:
    print("You can input only number")
except ZeroDivisionError:
    print("Ypu can not divide by zero")
except TypeError:
    print("Type of data dont same")
'''
try :
    num1 = int(input("number 1 = "))
    num2 = int(input("number 2 = "))
    result = num1/num2
    print(result)
except Exception as e:
    print(e)
