
def getprimefactors(integer):
    a = list()
    divisor = 2
    integer = int(integer)
    while(divisor <= integer):
        if(integer%divisor) == 0:
            a.append(divisor)
            integer = integer / divisor
        else:
            divisor+= 1
    print(a)

if __name__ == "__main__":
    integer = input("Enter the number")
    getprimefactors(integer)