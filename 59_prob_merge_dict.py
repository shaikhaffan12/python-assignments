dict1 = {'first':1, 'second':2}
dict2 = {'third':3, 'fourth':4}

# Using **kwargs it pass all the arguments from 1st dict and 2nd dict to third dict
dict3 = {**dict1 , **dict2} 

print(dict3)

# Second Approach

# using update method of dictionary it update 1st dictionary with second dictionary
dict1.update(dict2)

print(dict1)