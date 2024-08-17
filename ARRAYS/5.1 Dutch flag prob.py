# def partition(pivot_i , a):
#     pivot = a[pivot_i]
#     smaller , equal , larger  = 0 , 0 , len(a)
#     while equal < larger:
#         if a[equal] < pivot:
#             a[smaller] , a[equal] = a[equal] , a[smaller]
#             smaller +=1
#             equal +=1
#         elif a[equal] == pivot:
#             equal +=1
#         else:
#             larger -=1
#             a[equal] , a[larger] = a[larger] , a[equal]
#     return
# A=[0,1,2,0,2,1,1]
# b=2
# partition(b,A)
# print(A)
    
def partiotion(pivot_i , a):
    pivot = a[pivot_i]
    # ARRANGE THE ELEMNETS SMALLER THEN THE PIVOT TO THE LEFT
    smaller = 0
    for i in range(len(a)):
        if a[i] < pivot:
            a[i] , a[smaller] = a[smaller] , a[i]
            a[smaller] +=1
    
    # ARRANGE THE ELEMNETS LARGER THEN THE PIVOT TO THE RIGHT

    larger = len(a) - 1
    for i in reversed(range(len(a))):
        if a[i] > pivot:
            a[larger] , a[i] = a[i] , a[larger]
            larger -=1

A = [0,1,2,0,2,1,1]
P = 3
partiotion(P,A)
print(A)                # Time complexcity O(n) & space O(1)