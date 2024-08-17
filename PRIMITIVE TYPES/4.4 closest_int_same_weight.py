def closest_int_with_same_weight(x):
    num_unsigned_bits = 64
    for i in range (num_unsigned_bits - 1):
        if (x >> i)&1 != (x >> (i +1)&1 ):
            x ^= (1 << i) | (1 << (i + 1))
            return x
    raise ValueError ("All bits are 0 and 1")
print (closest_int_with_same_weight(1))