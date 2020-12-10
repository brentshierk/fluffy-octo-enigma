from person import Person
import random

#all attributes are public except for salary and the employeeId
class Employee(Person):
    _salary = 0
    def __init__(self,name,age,position):
        super().__init__(name,age)
        self.position = position
        self._employeeId = random.randrange(1000,9999)
        self.workstatus = bool
        self.team = str()
        
        #create instanced varible for work status.

    # def submitWork(self,workStatus):
    #     if self.workStatus == 'compleate':
    #         self.workstatus == True
        
    #     else self.workStatus == 'incompleate':
    #         self.workstatus == False
    #     return self.workstatus
    def _setSalary(self,amount):
        new_salary = amount + self._salary
        self._salary = new_salary
        print(f"your starting salary is : {self._salary}$")


    def _askForRaise(self):
        result = random.randrange(2)

        if result == 0:
            print('yeah you can have a raise')
            new_salary = self._salary + 1000
            self._salary = new_salary
            print(f"your new salary is : {self._salary}$")
            
        else:
            print('nope maybe next year.')
        return self._salary

    
    def sayHello(self): #this should override the persons sayHello method.
        print(f'Hello my name is {self.name} and im {self.age} and im a {self.position}.')
    


