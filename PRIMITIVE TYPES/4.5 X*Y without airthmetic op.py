def mul (x,y):
    def add (a,b):
        running_sum , carry , k , temp_a , temp_b = 0,0,1,a,b
        while temp_a or temp_b :
            ak , bk = a & k , b & k
            carryout = (ak & bk) | (ak & carry) | (bk & carry)
            running_sum |= ak ^ bk ^ carry
            carry , k , temp_a , temp_b = carryout << 1 , k << 1 , temp_a >> 1 , temp_b >> 1
        return running_sum | carry
    
    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum , y)
        x , y = x >>1 , y<<1
    return running_sum

print (mul(13,9))
