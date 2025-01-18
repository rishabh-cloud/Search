
def bsort(list):
    l=len(list)
    for i in range(l):
        for j in range(0,l-i-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

list=[1,3,24,4,6,86,9,12,45]
list1=[]
bsort(list)
print(list)
print(list[-3:])


