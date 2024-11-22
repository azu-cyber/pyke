def numberOfBits(n):
    ones = 0
    zeros=0
    while (n):
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        n >>= 1
    print("\n\nOnes = ", ones, "\nZeros ", zeros)
number = int(input("Enter your number : "))
numberOfBits(number)
    #project 2
def setOrNot(number, n) :
        if number & (1 << (n - 1)):
            print ( "\nSET")
        else:
            print ( "\nNOT SET")
number = int(input("Enter number : "))
n = int(input("Enter bit number : "))
setOrNot(number, n)