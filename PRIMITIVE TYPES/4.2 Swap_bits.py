def swap_bits(x,i,j):
    if (x >> i)&1 != (x >> j)&1:
        bit_mask= (1 << i) | (1 << j)
        x ^= bit_mask                       # x ^ 1 = 0 when x = 1 [gives 0 when values are same 1^1=0, 1^0=1 and vice versa]
    return x

print(swap_bits(73, 1, 6))
