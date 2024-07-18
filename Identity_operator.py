#Compare two objects

a=[1,2]
b=[1,2]
a=b
print(id(a))
print(id(b))

print(a is b)