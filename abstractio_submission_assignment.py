
#import abstractmethod from modules
from abc import ABC, abstractmethod

#Creat ABC class
class El_Rodeo(ABC):
    #Function for Bill
    def Bill(self, amount):
        print("Your purchase amount is: ",amount)
    #Abstract function to pass an argument
    @abstractmethod
    def payment(self, amount):
        pass

#Create child class
class DebitCardPayment(El_Rodeo):
    #Function to combine parent and child class through abstraction
    def payment(self, amount):
        print('Thank you for your purchase of {}'.format(amount))

#Creation of object
obj = DebitCardPayment()
obj.Bill("$32.75")
obj.payment('$32.76')
                
        
    











