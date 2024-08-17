def reach(a):
    further_reached , last_index = 0 , len(a) - 1
    i = 0
    while i <= further_reached and further_reached < last_index:
        further_reached = max(further_reached , a[i] + i)
        i += 1
    return further_reached >= last_index

A = [3,3,1,0,2,0,1]
print(reach(A))                         # Time complexcity O(n)