tupl = ("banana","apple","mango")

# Tuple Is Immutable So We Cannot Modify Tuple
# So we need to convert tuple to list then modify list
# then cconver list return into tuple thats how we modify tuple

lis = list(tupl) # convert tuple to list
lis.append("grapes")
lis.append("dragon fruit") # append new values to the List

tupl1 = tuple(lis) # convert list to tuple
print(tupl1)
