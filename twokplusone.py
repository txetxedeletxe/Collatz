def classDescomposition(x):
    temp = x
    l = []
    while temp != 0:
        if (temp % 2 == 0):
            l.append("2*" + str(int(temp/2)))
            temp /= 2
        else:
            l.append("2*" + str(int((temp-1)/2)) + "+1")
            temp = (temp-1)/2
    return l;

def collatz(x):
    if (x % 2 == 0):
        return x / 2
    else:
        return 3*x+1
    

def cyclesToReduction(x):
    temp = x
    i = 0;
    while not temp < x:
        temp = collatz(temp)
        i+= 1

    return i

def code():
    for i in range(2,1000):
        if (not i % 3 == 0 and not i % 2 == 0 and i % 4 == 3):
            print(str(i) + " class descomposition: " + str(classDescomposition(i)) + ", cycles to reduction: " + str(cyclesToReduction(i)))

if __name__ == "__main__":
    code()
