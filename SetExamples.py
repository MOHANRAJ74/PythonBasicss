#Set Examples

name={'Arun','Bala','Chandru','Dineh','Siva'}

print(name)
print(type(name))

for nn in name:
    print(nn)
#Adding new element
print("<-------------------->")
name.add('Raja')
print(name)

a={'Mohan','Kumar','Ajay'}
name.update(a)
print(a)

for jj in name:
    print(jj)
print("<-------------------->")
a={1,2,3,4,5,6}
b={'a','b','c','d','e','f'}

c=a.union(b)
print(c)
a.update(b)
print(a)
