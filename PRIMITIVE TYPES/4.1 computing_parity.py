# # COMPUTING THE PARITY OF A WORD:

# #                                                                     1

# def parity(x):
#     result = 0
#     while x:
#         result ^= x & 1
#         x >>= 1
#         return result
    
# print(parity(1011))




# #                                                                     2

# def parity(x):
#     result = 0          # DOUBT 1/0
#     while x:
#         result ^=  1
#         x &= x - 1
#     return result

# print(parity(1011))



# #                                                                    3


# def parity(x):
#     mask_size = 16
#     bit_mask = 0xffff

#     return (precomputed_parity[x >> (3 * mask_size)] ^
#             precomputed_parity[x >> (2 * mask_size) & bit_mask] ^
#             precomputed_parity[(x >> mask_size) & bit_mask] ^
#             precomputed_parity[x & bit_mask]
           
#            )
           
# #                                                                    4
# def parity(x):
#     x ^= x >> 64
#     x ^= x >> 16
#     x ^= x >> 8
#     x ^= x >> 4
#     x ^= x >> 2
#     x ^= x >> 1
#     return x & 0x1

# print(parity(1011))