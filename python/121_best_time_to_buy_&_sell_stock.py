def maxProfit(self, prices: list[int]) -> int:
    pl = 0
    pr = 1
    mp = 0
    while pr < len(prices):
        if prices[pl] < prices[pr]:
            print(f"{prices[pl]} < {prices[pr]}")
            profit = prices[pr] - prices[pl]
            mp = max(mp, profit)
        else:
            pl = pr
        pr += 1
    print(mp)
    return mp