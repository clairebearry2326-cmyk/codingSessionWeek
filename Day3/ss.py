def is_passing(score):
    if (score >= 60):
        return True
    else:
        return False

number = int(input("Enter any number: "))
isOverSixty = is_passing(number)

print(str(isOverSixty))