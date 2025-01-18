
def sumoflist(lis):
    sum=0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

def muloflist(list):
    mul=1
    for i in range(len(list)):
        mul = mul * list[i]
    return mul


list=[2,3,5,10,15]

print("total value",sumoflist(list))
print("Mul value",muloflist(list))

