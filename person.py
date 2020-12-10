class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
    
    def sayHello(self):
        #simple print statement that displayes a persons name and age.
        print(f"hello my name is {self.name} and im {self.age}.")
    
    def talkTo(self,person):
        print(f"Hey {person.name},havent seen you in awhile! how are the cats?")


# lindsay = Person('lindsay',22)
# #lindsay.sayHello()
# james = Person('james',55)
    
    
        