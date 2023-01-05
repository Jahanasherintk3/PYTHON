a  = [0,1,2,10,99]
b = bytes(a)
print(b)
c = bytearray(a)
print(c)

#b[0] = 100
#print(b)
c[0] = 100
print(c)

a=-23
print(a)
print(type(a))