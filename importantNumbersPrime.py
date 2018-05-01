numRange = 1000
def prime(x):
    top = int(x**(1/2)) + 1
    for i in range(2,top):
        if (x % i == 0):
            return False
    return True
        
def importantNumber(x):
    return x % 2 != 0 and x % 3 != 0
def code():
    for i in range(1,numRange):
        if importantNumber(i):
            if prime(i):
                print(str(i) + ": Prime")
            else:
                print(str(i) + ": Not prime")





if __name__ == "__main__":
    code()
