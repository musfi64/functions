def add(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def div(x,y):
    return x/y
print(" pls select the operation")
print("a. add")
print("s.subtraction")
print("m.multiply")
print("d.div")
choise=str(input("pls enter your choise"))
num1=int(input("pls enter your number"))
num2=int(input("pls enter your number"))
if choise=="a":
    print(add(num1,num2))
elif choise=="s":
    print(subtraction(num1,num2))
elif choise=="m":
    print(multiply(num1,num2))
elif choise=="d":
    print(div(num1,num2))
else:
    ("invalid input")