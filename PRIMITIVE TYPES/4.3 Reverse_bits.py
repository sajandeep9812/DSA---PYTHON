precomputed_reverse = []

def first_reverse_bit(x):
    mask_size = 16
    bit_mask = 0xffff

    y = (precomputed_reverse [ x & bit_mask] << (3 * mask_size) |
         precomputed_reverse [ (x >> mask_size) & bit_mask] << (2 * mask_size) |
         precomputed_reverse [ (x >> (2*mask_size)) & bit_mask] << mask_size |
         precomputed_reverse [ (x >> (3*mask_size)) & bit_mask] 
        )
    
    return y
