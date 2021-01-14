# open("name of file","mode","เข้ารหัส")
#write
'''
try:
    fw = open("Score.txt","w",encoding="utf-8")
    fw.write("Hello World\n")
    fw.writelines("Hi Hi")
    fw.close()
except FileNotFoundError:
    print("File not found")
'''
#read
'''
try:
    fr = open("Score.txt","r",encoding="utf-8")
    line = fr.readlines()
    for x in line:
        print(x)
    fr.close()
except FileNotFoundError:
    print("File not found")
'''
#append
'''
try:
    fa = open("Score.txt","a",encoding="utf-8")
    fa.writelines("adding line\n")
    fa.write("adding line2\n")
    fa.close()
except FileNotFoundError:
    print("File not found")
'''
#delete text
'''
import os
try:
    if os.path.exists("Score.txt"):
        os.remove("Score.txt")
    else:
        print("file doesn't exist")
except Exception as e:
    print(e)
'''