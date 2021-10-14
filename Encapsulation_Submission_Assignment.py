

#Creation of class Number
class Number:
    #initialization of class
    def __init__(self):
        #Creating protected Var
        self._protectedVar = 35
        #Creating PrivateVar
        self.__privateVar =42
    #Getting the Private Var and printing it

    def getPrivate(self):
        print(self.__privateVar)
    #setting a new value in Private Var

    def setPrivate(self, private):
        self.__privateVar = private
#Creating object and changing protected Var and printing.
obj = Number()
obj._protectedVar = 12
print(obj._protectedVar)

#Creating object and getting private Var, changing it, and then running the get function again

obj = Number()
obj.getPrivate()
obj.setPrivate(12)
obj.getPrivate()






    

    
    





























