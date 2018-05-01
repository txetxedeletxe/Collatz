numRange = 1000
def criticalNumber(x):
    return x % 24 == 5 or x % 24 == 13
def collatzCycle(x):
    temp = x
    l = [temp]
    while temp != 1:
        temp = temp*3+1
        while temp % 2 == 0:
            temp = temp // 2

        if criticalNumber(temp):
            l.append(str(temp) + "!")
        else:
            l.append(str(temp))
        

    return l
def code():
    j = 1
    for i in range(1,numRange):
        if (i % 3 != 0 and i % 2 != 0):
            print(str(j)+". "+ str(i) + ": " + str(collatzCycle(i)))
            j += 1


if __name__ == "__main__":
    code()
