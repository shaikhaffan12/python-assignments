dict1 = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fith':5, 'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
lis = [] # Create Empty list to store unique value 
for i in dict1.values():
    if i in lis:
        continue
    else:
        lis.append(i) # append only unique value from dictionary

print(lis)