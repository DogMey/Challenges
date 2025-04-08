class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        sell=0
        for i in range(len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            elif (prices[i]-buy)>0:
                sell+=prices[i]-buy
                buy=prices[i]
        return sell
    
solucion = Solution()

# Definir los precios de las acciones
prices = [7,1,5,3,6,4]

print(solucion.maxProfit(prices))