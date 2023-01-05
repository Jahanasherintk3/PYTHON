a=[2,4,6,8]
b=bytearray(a)   #bytearray is mutable,which means it can change
b[0]=100

for x in b:
    print(x)

b[0]=88
for x in b:
    print(x)