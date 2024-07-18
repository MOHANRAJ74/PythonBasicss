
a=(1,2.5,True,"Ram")

print(a)
print(type(a))
print(a[0])
print(a[-1])
print(a[0:3])
b=list(a)
print(b)
b.append("Raja")
print(b)
a=tuple(b)
print(a)

for i in a:
    print(i)

if "Raja" in a:
    print("Raja is Found")
else:
    print("Not Found")