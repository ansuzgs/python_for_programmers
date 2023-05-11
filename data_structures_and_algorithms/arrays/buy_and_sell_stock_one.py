def buy_and_sell_stock_once(A):
    max_profit = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            profit = A[j] - A[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

def buy_and_sell_once(A):
    max_profit = 0
    min_price = float('inf')
    for price in A:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stock_once(A))
print(buy_and_sell_once(A))