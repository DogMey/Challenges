class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1   # Se inicializan dos punteros
        while left < right:                 # Mientras los punteros no se crucen
            current_sum = numbers[left] + numbers[right]    # Suma de los valores en los punteros
            if current_sum == target:                       # Si la suma es igual al objetivo
                return [left + 1, right + 1]                # Se devuelve la posición (1-indexed)
            elif current_sum < target:      # Si la suma es menor que el objetivo
                left += 1                   # Se mueve el puntero izquierdo hacia la derecha
            else:                           # Si la suma es mayor que el objetivo
                right -= 1                  # Se mueve el puntero derecho hacia la izquierda
        return []
    
Solution = Solution()
# Ejemplo de uso
numbers = [2, 7, 11, 15]
target = 9
print(Solution.twoSum(Solution, numbers, target))