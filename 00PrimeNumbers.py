

def G_get_prime_number(a):
    print("Given Input is {0}".format(a))
    primenumbers = [2,3,5,7]
    factors = []
    for i in primenumbers:
        print("Current Operator is {}".format(i))
        print("Result of the Operator is {}".format(a % i))
        if(a % i == 0):
            print("Entered the Loop")
            factors.append(i)
            a = a / i
        else:
            print("Skipped the Loop")

    print(factors,primenumbers)

def get_prime_number(a):
    factors = []
    divisor = 2
    while(divisor <= a):
        if(a % divisor) == 0:
            factors.append(divisor)
            a = a / divisor
        else:
            divisor += 1
    print("Factors from solution are {}".format(factors))
    return factors




if __name__ == "__main__":
    get_prime_number(630)
    # G_get_prime_number(630)