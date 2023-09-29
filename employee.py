class Employee:
    def __init__(self,getfirstname,getlastname):
        self.getfirstname = getfirstname
        self.getlastname = getlastname

    def greet(self):
        print(f"first name is {self.getfirstname} and last name is {self.getlastname}")

emp1 = Employee("Alok","Bedwal")
emp2 = Employee("Deepak","lakhlan")


emp1.greet()
emp2.greet()



