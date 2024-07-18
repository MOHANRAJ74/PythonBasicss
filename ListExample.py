#List Examples
from builtins import type

a=[1,2,3,4,5,6,7,8,9]

print("Print all: ",a)
print("Type of A: ",type(a))
a[0]=100
print("<-----------Slicing---------->")
print("Print all: ",a)
print("Print Reverse Order last element: ",a[-1])
print("Idex 0 to 3: ",a[0:3])
print("print index 2 to end: ",a[2:])
print("Index from 0 upto 3: ",a[:5])
print("<-------------------------->")
a=[1,True,'Ram',2.5,[1,2,3,4,5]]
print(a)
print("Type of A: ",a)
print(a[0]," is Type is: ",type(a))
print(a[1]," is Type is: ",type(a))
print(a[2]," is Type is: ",type(a))
print(a[3]," is Type is: ",type(a))
print(a[4]," is Type is: ",type(a))
print("<--------------------------->")
a=[10,20,30,40,50,60,70,80]
print(a)
b=a.copy()
print("Print B: ",b)
print("Count of B: ", len(a))
a.remove(10)
a.pop(2)
print("After Remove: ",a)
