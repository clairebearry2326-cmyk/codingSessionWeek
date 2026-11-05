numlist = [6, 2, 5, 13, 1]
dusa = numlist[0]

for i in range(1,len(numlist)):
    yobi = numlist[i]
    if dusa > yobi:
        dusa = dusa+yobi
    else:
        break

print(dusa)