tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
l = list(tuple1) #convert list to tuple for iterating through for loop
# print(l)

for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i][1] > l[j][1]:
            l[i],l[j] = l[j],l[i]

print(l)