list = []
nonlist = []
for x in range(5):
    num = int(input("Enter a number"))
    if num > 0:
        list.append(num)
    else:
        nonlist.append(num)
print(len(list))
