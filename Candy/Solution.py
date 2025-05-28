class Solution(object):
    def candy(self, notas):
        if not notas: # Si no hay notas no hay dulces
            return 0
        
        n = len(notas)
        candies = [1] * n # Cada niño recibe al menos un dulce
        
        # Se recorre de izquierda a derecha y se le da un dulce mas si i es mayor que i-1
        for i in range(1, n):
            if notas[i] > notas[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Se hace lo mismo de derecha a izquierda
        for i in range(n - 2, -1, -1):
            if notas[i] > notas[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies) # Se suman los dulces de todos los niños
    
solucion = Solution()

notas = [1,2,2]
print(solucion.candy(notas))