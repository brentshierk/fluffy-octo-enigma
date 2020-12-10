from person import Person
from employee import Employee
from team import Team
class Company:
    
    def __init__(self,name,_revenue,services):
        self.name = name
        
        self._revenue = _revenue 
        
        self.services = services 

    def AddManagerToTeam(self,name,age,position,team):
        createNewManager = Employee(name,age,position)
        addToTeam = team.addMemebers(team,name)
        print(f'{self.name},{team.name}')
        return addToTeam,createNewManager
        
        
    def AnnounceRevenue(self):
        print(f"our revenue for this quarter is : {self._revenue}")
        

#People class methods
michael = Person('michael',50)
lindsay = Person('lindsay',22)
lindsay.sayHello()
lindsay.talkTo(michael)
#employee class methods
brent = Employee('brent',24,'backend dev')
brent._setSalary(3000)
brent._askForRaise()
brent.sayHello()
#team class methods
developers = Team('developer','voice chat',None)
jake = Employee('jake',35,'senior dev')
developers.addMemebers('developers',jake)
developers.GiveWork('add voice filters')
#company class methods
google = Company('google','3b','search engine')
google.AddManagerToTeam('jacob',30,'tech lead',developers)
google.AnnounceRevenue()






