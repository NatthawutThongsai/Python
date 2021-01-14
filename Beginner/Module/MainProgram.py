from MyPackage.CalculateService import addition
import MyPackage.Weather as w
addition(30,40,60)
print(w.city["นนทบุรี"])
#Module Date / Time
import datetime
result = datetime.datetime.now()
print(result)
print(result.year)
print(result.strftime("%x"))
newdate = datetime.datetime(2020,6,20)
print(newdate)