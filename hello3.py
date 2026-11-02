integerOne=int(input("score:"))
if integerOne%2==1:
    print("odd")
else:
    print("even")
if integerOne>=60:
    print("pass")
else:
    print("fail")
num1=int(input("num1:"))
num2=int(input("num2:"))
num3=int(input("num3:"))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)