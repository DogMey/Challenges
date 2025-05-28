class Solution(object):
    def trap(self, height):
        if not height:  # Si no hay alturas, no hay agua atrapada
            return 0

        n = len(height) 
        left_max = [0] * n  # Lista para almacenar el máximo a la izquierda
        right_max = [0] * n # Lista para almacenar el máximo a la derecha

        left_max[0] = height[0] # El máximo a la izquierda del primer elemento es el mismo
        for i in range(1, n):   # Se recorre de izquierda a derecha
            left_max[i] = max(left_max[i - 1], height[i])   # El máximo a la izquierda es el máximo entre el actual y el anterior

        right_max[n - 1] = height[n - 1]    # El máximo a la derecha del último elemento es el mismo
        for i in range(n - 2, -1, -1):      # Se recorre de derecha a izquierda
            right_max[i] = max(right_max[i + 1], height[i]) # El máximo a la derecha es el máximo entre el actual y el siguiente


        water_trapped = 0   # Variable para almacenar el agua atrapada
        for i in range(n):  # Se recorre cada posición
            water_trapped += min(left_max[i], right_max[i]) - height[i] # El agua atrapada es el mínimo entre el máximo a la izquierda y el máximo a la derecha menos la altura actual

        return water_trapped
    
solucion = Solution()

traps = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solucion.trap(traps))