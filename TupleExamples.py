#Tuple Example

a=(1,2.5, True, "Ram")

print("Print All: ",a)
print("Type of A: ",type(a))
print("Print 0: ",a[0])
print("print last index: ",a[-1])
print("print O to 2",a[0:2])
b=list(a)
print(b)
print("Type B: ",type(b))
b.append("Raja")
print(b)
print(type(b))
a=tuple(b)

print("Type: ",type(a))
print("<-------------------->")
for i in a:
    print(i)
print("<-------------------->")
if "Raja" in a:
    print("Raja is Found")
else:
    print("Not Found")
