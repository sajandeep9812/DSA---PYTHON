def delete_duplicate(a):
    if not a:
        return 0
    
    write_index = 1
    for i in range(1 , len(a)):
        if a[write_index - 1] != a[i]:
            a[write_index] = a[i]
            write_index += 1
    return write_index

A =[2,3,5,5,7,11,11,11,13]
print(delete_duplicate(A))              # Return the number of valid entries || TIME COMPLEXITY O(n) and Space Complexity O(1) ||