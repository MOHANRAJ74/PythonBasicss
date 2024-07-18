#Try block

try:
    a=10/8
except Exception as e:
    print(e)
else:
    print("Value of A: ",a)
finally:
    print("Thanks")
