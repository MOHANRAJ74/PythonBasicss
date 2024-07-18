#Class and Methods

class Student:
    name="Mohanraj"
    age=24

    def printall(self):
        print("Name: ",Student.name)
        print("Age: ",Student.age)

Student.printall(self)
print(Student.__dict__)

print(getattr(Student, "Printall"))