
class mycls:
    def __init__(self):
        self.set1 = {20,30,40,'jack',50}
        self.set2 = {60,70,20,40,'jack'}
        self.set3 = set() # Create empty set to store identical items

    def get_iden(self):
        for i in self.set1:
            if i in self.set2:
                self.set3.add(i) # use add method of set to add items to third set
        print(self.set3)

myobj = mycls()
myobj.get_iden()