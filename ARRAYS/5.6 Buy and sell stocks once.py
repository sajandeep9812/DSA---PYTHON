A =[310,315,275,295,260,270,290,230,255,250]
# def buy_sell(A):
#     max_profit = 0
#     for i in range(len(A)-1):
#         for j in range(i+1 , len(A)):
#             if A[j] - A[i] > max_profit:
#                 max_profit = A[j] - A[i]
#     return max_profit
# print(buy_sell(A))              # TIME COMPLEXITY IS HIGH O(N^2) AND SPACE COMPLEXITY IS ___ ||  NOT AN OPTIMAL SOLUTION.

def buy_sell(A):
    max_profit = 0.0
    min_price = A[0]

    for price in A:
        min_price = min(min_price , price)
        compare_profit = price - min_price
        max_profit = max(max_profit , compare_profit)
    return max_profit
print(buy_sell(A))                 # TIME COMPLEXITY O(N) AND SPACE COMPLEXITY IS 0(1).