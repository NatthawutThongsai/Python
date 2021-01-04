st = " xyz  "
st2 = "xxxyyyyzzz"
print(len(st))
print(st.strip())
print(len(st.lstrip()))
print(len(st.rstrip()))
print(st.upper())
print(st.lower())
print(st.capitalize())
print(st.replace("xyz","abc"))
print(st2.replace("x","y",2))
print("xxx" in st2)
fname = "Natthawut"
lname = "Thongsai"
text = "Firstname : {}\t Lastname : {}\tAge : {}"
print(text.format(fname,lname,"20"))
print(st2.count("x"))
print(st2.startswith("x"))
print(st2.endswith("z"))