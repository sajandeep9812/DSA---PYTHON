import math
def palindrom(x):
    if x <= 0:
        return x==0
    
    numberofdigits = math.floor(math.log10(x))+1
    msd_mask = 10 ** (numberofdigits - 1)
    for i in range (numberofdigits // 2):
        if x // msd_mask != x % 10:             #if msb not equal to lsb
            return False
        x %= msd_mask                           # removes msb
        x //= 10                                # removes lsb

        msd_mask //= 100
    return True
print (palindrom(1234321))