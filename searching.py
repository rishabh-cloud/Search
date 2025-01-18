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

#binary search
def bsearch(list1,n1):
    l=0
    h=len(list1)
    while l<=h:
        mid=(l+h) //2
        if list1[mid]>n1:
            h=mid-1
        elif list1[mid]<n1:
            l =mid+1
        else:
            return mid
    return -1

list1=[2,4,6,7,8,22,25,100]
n1=22
result1=ser(list1,n1)
if result1 !=-1:
    print("element found",result1)
else:
    print("not found")