class Person:
    name = 'Unknown'
    age = 'Unknown'
    gender = 'Unknown'

    
    def information(self):
        msg = "\nName: {} \nAge: {}".format(self.name,self.age)
        return msg
        

class Teacher(Person):
    name = 'Rachel'
    age = '46'
    gender = 'Female'
  

    def overworked(self):
        msg = "\nWorks 80 hours a week and paid for forty"
        return msg








if __name__ == "__main__":
    
    teacher = Teacher()
    print(teacher.information())
    print(teacher.overworked())





















