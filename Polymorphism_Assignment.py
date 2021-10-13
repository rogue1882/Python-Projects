#Parent Class User
class User:
    name = "Mark"
    email = "mark@gmail.com"
    passwork = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

# Child Class 1 Employee
class Employee(User):
    base_pay = 23.00
    department = "janitorial"
    pin_number = "1213"
#Same method except the requested information now is a pin number
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))

        else:
            print("The pin or email is incorrect.")


# Child Class 2 Contractor
class Contractor(User):
    Hourly_Cost = 125.00
    Trade = "Electrician"
    Contractor_id = "1213"
#Same method changing password to Contractor_ID 
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pinContractor_id = input("Enter your Contractor ID: ")
        if (entry_email == self.email and entry_pin == self.Contractor_id):
            print("Welcome back, {}!".format(entry_name))

        else:
            print("The pin or email is incorrect.")

if __name__ == "__main__":
            
    customer = User()
    customer.getLoginInfo()

    manager = Employee()
    manager.getLoginInfo()

    bill = Contractor()
    bill.getLoginInfo()
