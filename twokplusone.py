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

def code():
    for i in range(1,100):
        print(str(i) + " class descomposition: " + str(classDescomposition(i)))

if __name__ == "__main__":
    code()
