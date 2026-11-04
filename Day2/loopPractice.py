#calculate the sum of all numbers
#from 1 to user provided number
user = int(input("Enter number:"))
output = 0
number = 1
while number <= user:
    output = output + number
    number = number + 1
    
print(output)