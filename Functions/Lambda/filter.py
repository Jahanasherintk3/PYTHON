prices=[20,30,40,50]
new_Prices=list(filter(lambda n: True if n<100 else False,prices))
print(prices)
print(new_Prices)

prices=[40,50,40,50]
def belowHundred(n):
    if n<100:
        return True
    else:
        return False

new_Prices=list(filter(belowHundred,prices))
print(prices)
print(new_Prices)