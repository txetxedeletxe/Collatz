numRange = 1000
def important(x):
    return x % 2 != 0 and x % 3 != 0
def distance(x,y):
    flip = 0
    tempx = x
    i = 0
    if (x % 6 == 1):
        flip = 4
    else:
        flip = 2

    while tempx != y:
        i+=1
        tempx+=flip
        if flip == 2:
            flip =4
        else:
            flip = 2

    return i


def upOrDown(x):
    temp = x
    temp = temp*3+1
    while temp % 2 == 0:
        temp = temp // 2

    if (temp > x):
        return "up x" + str(distance(x,temp)) + ", to: " + str(temp)
    else:
        return "down x" + str(distance(temp,x))+ ", to: " + str(temp)


def code():
    j = 1
    for i in range(1,numRange):
        if (important(i)):
            print(str(j) + ". " + str(i) + ": " + upOrDown(i))
            j+=1


if __name__ == "__main__":
    code()
