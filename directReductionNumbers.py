nuIter = 1000
def reducedCollatz(x):
    temp = x*3+1
    while temp % 2 == 0:
        temp = temp // 2

    return temp

def reduceClass(x):
    
    if x % 12 != 1 and x % 12 != 5:
        return False
    else:
        temp = x
        while temp != 1:
            temp = reducedCollatz(temp)
            if temp > x:
                return False

        return True

def code():
    for i in range(1,nuIter):
        if (reduceClass(i)):
            print(i)



if __name__ == "__main__":
    code()
