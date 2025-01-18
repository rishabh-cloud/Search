def swap(list):
    n=len(list)
    print(n)
    #using 3rd variable
    temp=list[n-1] #9
    list[n-1]=list[0]
    list[0]=temp
    #print(temp)


    #list[0], list[-1] = list[-1], list[0]   #using swap method of python
    return list

list=[2,3,5,6,8,9]
print("original list",list)
swap(list)
print(f"swapped list",list)

