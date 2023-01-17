plusOne=lambda n:n+1
print(plusOne(10))

sum=lambda a,b,c :a+b+c 
print(sum(10,20,30))

#without lambda

a=int(input("enter first"))
b=int(input("enter second"))

def maxValue(a,b):
    return a if a>b else b
print(maxValue(a,b))