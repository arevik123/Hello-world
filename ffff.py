def getNextStreet(street):
    newlist = []
    for i in range(len(street)):
        if i == 0 and street[i+1] == 1:
            newlist.append(1)
        elif i > 0 and i < len(street) - 1 and street[i-1] + street[i+1] == 1:
            newlist.append(1)
        elif i == len(street) - 1 and street[i-2] == 1:
           newlist.append(1)
        else:
            newlist.append(0)

    return newlist


street = [1, 0, 0, 1, 0, 1, 1, 1]

print(street)

for j in range(10):
    street = getNextStreet(street)
    print(street)