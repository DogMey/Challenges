class Solution(object):
    def maxProfit(self, prices):
        minPrecio=prices[0]
        maxBeneficio=0
        for i in range(len(prices)):
            if prices[i]<minPrecio:
                minPrecio=prices[i]
            elif prices[i]-minPrecio>maxBeneficio:
                maxBeneficio=prices[i]-minPrecio
        return maxBeneficio

solucion = Solution()

# Definir los precios de las acciones
prices = [1,2,3,4,5,6,7]

print(solucion.maxProfit(prices))