#Dictionary Examples

user={
    "name":"Ram",
    "age":15,
    "City":"Kovai",
    "Email":"ramkumar@gmail.com"
}
print(user)
print(type(user))
print(user["name"])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())
print("<-------------------->")
for x in user:
    print(x,":",user[x])