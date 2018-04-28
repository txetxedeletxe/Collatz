def factors(x):
    fact = []
    i = 2
    temp = x
    while temp != 1:
        while temp % i == 0:
            fact.append(i)
            temp /= i

        i += 1

    return fact


def code():
    j = 1;
    for i in range(2000):
        if (i % 3 == 0 and i % 2 == 1):
            print(str(j)+". factors i=" + str(i) + ": " + str(factors(i)));
            print(str(j)+". factors i+1=" + str(i+1) + ": " + str(factors(i+1)));
            j += 1;



if __name__ == "__main__":
    code()



