num1=int(input("Enter NUMBER 1:\n"))
num2=int(input("Enter NUMBER 2:\n"))
num3=int(input("Enter NUMBER 3:\n"))
num4=int(input("Enter NUMBER 4:\n"))
num5=int(input("Enter NUMBER 5:\n"))
num6=int(input("Enter NUMBER 6:\n"))

if(num1>num6):
    f1=num1
else:
    f1=num6

if(num2>num5):
    f2=num2
else:
    f2=num5
if(num3>num4):
    f3=num3
else:
    f3=num4
if(f1>f2):
    print(str(f1) + " is the gretest")
elif(f3>f1):
    print(str(f3) + " is the gretest")
elif(f2>f3):
    print(str(f2) + " is the gretest")
else:
    print("I dont Know............")


