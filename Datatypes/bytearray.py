a=[2,4,6,8]
b=bytearray(a)   #bytearray is mutable,which means it can change
b[0]=100

l=[38,40,42,44]
b=bytes(l)
ba=bytearray(l)
print(l)
print(b)
print(type(l))
print(type(b))
print(type(ba))

b[0]=88
for x in b:
    print(x)