''''a=int(input("enter first num"))
b=int(input("enter second num"))
def maxValue(a,b):
        return a if a>b else b
print(maxValue(a,b))'''   #without lambda


'''a=int(input("enter first num"))
b=int(input("enter second num"))
def maxValue(a,b):
    if a>b:
        return a
    else:
        return b
print(maxValue(a,b))''' #it is another way without lambda

a=int(input("enter first num"))
b=int(input("enter second num"))
maxValue=lambda a,b: a if a>b else b
print(maxValue(a,b))  #this is with lambda only


#three ways of wrinting functional program