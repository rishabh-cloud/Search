def ser(list,n):
    for i in range(len(list)):
        if list[i]==n:
            return i
    return -1

list=[2,4,6,78,2,5,10]
n=11
result=ser(list,n)
if result !=-1:
    print("element found")
else:
    print("not found")