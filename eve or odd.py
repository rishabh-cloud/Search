def even_odd(list):
    even=[]
    odd=[]
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    #print(odd)
    return even,odd


list=[1,3,24,4,6,86,9,12,45]
out=even_odd(list)
print("even element",out[0])
print("odd elment",out[1])

for i in range(1,10):
    if i % 2!=0:
        print("odd values: ",i)


val=[-4,4,6,5]
val1=[]
for i in val:
    if i > 0:
        #print("positve value",i)
        val1.append(i)
print(val1)


a=-5
b=4
for i in range(a,b):
    if i >0:
        print("postive",i)