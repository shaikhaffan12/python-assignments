class mycls:

    def poly(self,side):
        print((side-2)*180,"Degree") # getting polygon degree

side = int(input("Enter the sides : "))

obj= mycls()
obj.poly(side)