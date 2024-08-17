def odd_even(A):
    even , odd = 0 , len(A) - 1
    while even < odd:
        if A[even] % 2 == 0:
            even += 1               # even = even + 1
        else:
            A[even] , A[odd] = A[odd] , A[even]
            odd -= 1
            
B=[3,5,8,10,11,2,0]
odd_even(B)
print(B)