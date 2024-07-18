class student:
    def __init__(self):
        self.name="Mohanraj"
        self.rno="15MCL074"
    def display(self):
        print("Student Name: ",self.name)
        print("Roll No: ",self.rno)

s1=student()

print(s1.name)
print(s1.rno)
s1.display()