class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1    # Se inician los punteros izquierdo y derecho
        max_area = 0                        # Variable para almacenar el área máxima
        
        while left < right:                 # Mientras los punteros no se crucen
            width = right - left                                # Calculamos el ancho entre los dos punteros
            current_height = min(height[left], height[right])   # Tomamos la altura mínima entre los dos punteros
            current_area = width * current_height               # Calculamos el área actual
            
            max_area = max(max_area, current_area)       # Actualizamos el área máxima si el área actual es mayor
            
            if height[left] < height[right]:            # Si la altura del puntero izquierdo es menor que la del derecho
                left += 1                               # Movemos el puntero izquierdo hacia la derecha
            else:                                       # Si la altura del puntero derecho es menor o igual
                right -= 1                              # Movemos el puntero derecho hacia la izquierda
        
        return max_area
    
Solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution.maxArea(height))