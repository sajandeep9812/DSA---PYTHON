# def count_bits(x):
#     num_bits = 0
#     while x:
#         num_bits += x & 1
#         x >>= 1
#     return num_bits

# num_bits = count_bits(1123)
# print(num_bits)


##########  BITWISE OPERATIONS  ##########

a=5
b=4

print(id(a))
print(id(b))

print(a&b)          # (AND Operation) Return 1 if both bits are one.
print(a|b)          # (OR Operation)  Return 1 if any of the bit is 1.
print(~a)           # (NOT Operation (compliment)) 2s compliment. eg = ~5 = -(5+1) which is -6.
print(a^b)          # (XOR Operation) If both bits are same then return 0 , otherwise return 1. 1^1=0, 1^0=1 and vice versa
print(a >> 2)       # (RIGHT SHIFT) We loose bits   [Ans = 1]
print(a << 2)       # (LEFT SHIFT)  We gain  bits  (a * 2**n)  [Ans = 20]


