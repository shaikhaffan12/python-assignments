def prog():
    objone = input("Enter Something: ")
    objtwo = input("Enter Something: ")

    if type(objone) == type(objtwo):
        if objone == objtwo:
            return True

        else:
            return False
    else:
        return False

obj = prog()
print(obj)