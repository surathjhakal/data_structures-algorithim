def buy_and_sell_stock_once(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)

    print(max_profit)

def main():
    n = int(input())
    prices = list(map(int, input().split()))
    buy_and_sell_stock_once(prices)

main()
