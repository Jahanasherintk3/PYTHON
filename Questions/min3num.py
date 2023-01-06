x=input("enter first num")
y=input("enter second num")
z=input("enter third num")

if x<y and x<z:
    min=x
elif y<z:
    min=y
else:
    min=z
print(min)