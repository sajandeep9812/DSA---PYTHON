def reverse (x):
    result , x_remaining = 0 , abs(x)              # abs gives absolute value (eg. -123 = 123)
    while x_remaining:
        result = result * 10 + x_remaining % 10    # "%" used to find lsb.
        x_remaining //= 10                         # "//" used to get floor value. Removes decimal value (eg. 7.6 = 7)
    return -result if x < 0 else result
print (reverse(1132))