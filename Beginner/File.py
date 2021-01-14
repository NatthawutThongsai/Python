# open("name of file","mode","เข้ารหัส")
try:
    fw = open("Score.txt","w",encoding="utf-8")
    fw.write("Hello World\n")
    fw.writelines("Hi Hi")
    fw.close()
except FileNotFoundError:
    print("File not found")
try:
    fr = open("Score.txt","r",encoding="utf-8")
    line = fr.readlines()
    for x in line:
        print(x)
    fr.close()
except FileNotFoundError:
    print("File not found")