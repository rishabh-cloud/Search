
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
def minimum(list):
    small=list[0]
    for i in list:
        if i <small:
            small=i
    return small
def maxi(list):
    big=list[0]
    for i in list:
        if i >big:
            big=i
    return big

list=[3,2,5,10,15]

print("total value",sumoflist(list))
print("Mul value",muloflist(list))
print("minimum value",minimum(list))
print("maxiumum value",maxi(list))

