class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        b = 0
        s = 1
        profit=0
        while b < n-1:
            while s<n:
                if prices[s]-prices[b] >=0:
                    profit = max(profit,prices[s]-prices[b])
                    s+=1
                else:
                    b=s-1
                    break
            b +=1
            s = b+1
        return profit
                

        