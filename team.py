from employee import Employee
from person import Person
class Team():
    members = list() 

    def __init__(self,team_name,product,workload):
         
        self.product = product
        self.team_name = team_name
        self.workload = workload

    def _GiveWork(self,work):
        
        self.workload = work
        print(f'new assignment : {self.workload}')
        return self.workload
           
    def addMemebers(self,team_name,employee):
        self.members.append(Employee)
        if len(self.members) == 0:
            print('no members in this team')
        else:
            print(f'horray we got a new hire to join the {self.team_name} team! we are now a team of {len(self.members)} welcome {employee.name}')
            
            #employee.team=str(team_name)
            #print(str(employee.team))


# 



