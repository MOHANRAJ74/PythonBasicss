#Init Method

class user:
    def __init__(self, name):
        print("Instance Called")
        self.name=name

    def printall(self):
        print("Name is: ",self.name)


#passing argument in constructor
ob=user("Mohanraj")
ob.printall()
print(ob.__dict__)
on=user("Rangasamy")
on.printall()
print(on.__dict__)