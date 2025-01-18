

list=[3,32,60,65,44,78,65,89]
list1=[3,32,60,65,44,78,65,89]

list1.pop() #it will remove last element

print(list1)
list1.remove(32)  #it will remove 32 from list
print(list1)
list1.pop(3)  #it will remove value from index3
print(list1)
rem=[32,89,78]
out=[]
for i in list:
    if i not in rem:
        out.append(i)
print(out)
