def del_ele(dict1,d_key): #taking dictioanry and element 
    if d_key in dict1:
        dict1.pop(d_key) # using dictionary pop method
        print(dict1)
    else:
        print("the key is not existing in dictionary.")
        print(dict1)

dict1 = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
dell_key = input("enter the key you want to delete from existing keys: ")

del_ele(dict1,dell_key)