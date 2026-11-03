num = int(input("Enter a number"))
print(num//60,"minutes,", num%60,"seconds")

score = int(input("Enter your score:"))
if score>=90:
    print("A")
elif score>=80:
    print("B")
else:
    print("C")