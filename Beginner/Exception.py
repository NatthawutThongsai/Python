try:
    num1 = int(input("number 1 = "))
    num2 = int(input("number 2 = "))
    result = num1/num2
    print(result)
except Exception as e:
    print(e)
else:
    print("End of program")
finally:
    print("End with finally")

while True:
    try :
        num1 = int(input("number 1 = "))
        num2 = int(input("number 2 = "))
        if num1==0 and num2==0:
            break
        if num1<0 or num2<0:
            raise Exception("ไม่สามารถป้อนค่าติดลบได้")
        result = num1/num2
        print(result)
    except ValueError:
        print("You can input only number")
    except ZeroDivisionError:
        print("You can not divide by zero")
    except TypeError:
        print("Type of data dont same")
    except Exception as e:
        print(e)

