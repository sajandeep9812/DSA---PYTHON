def power(x,y):
    result , power = 1.0 , y
    if y < 0:
        power , result = -power , 1.0/x
    while power:
        if power & 1:
            result *= x                      # result = result * x
        x , power = x * x , power >> 1
    return result
print (power(2.2,5))