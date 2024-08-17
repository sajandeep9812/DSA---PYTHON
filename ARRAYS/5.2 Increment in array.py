A = [1,3,5]
def plus_one(a):
    a[-1] +=1
    for i in reversed (range(1,len(a))):
        if a[i] != 10:
            break
        a[i] = 0
        a[i-1] +=1
    if a[0] == 10:
        a[0] = 1
        a.append(0)
    return a
print(plus_one(A))              # Time complexcity O(n)