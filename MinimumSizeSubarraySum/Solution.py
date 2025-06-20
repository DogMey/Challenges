class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)   # Longitud del array
        left = 0        # Puntero izquierdo de la ventana
        current_sum = 0             # Suma actual de la subarray
        min_length = float('inf')   # Inicializa el mínimo a infinito
        for right in range(n):      # Puntero derecho de la ventana
            current_sum += nums[right]  # Agrega el valor del puntero derecho a la suma actual
            while current_sum >= target:    # Mientras la suma actual sea mayor o igual al objetivo
                min_length = min(min_length, right - left + 1)  # Actualiza el mínimo de longitud
                current_sum -= nums[left]   # Resta el valor del puntero izquierdo de la suma actual
                left += 1   # Mueve el puntero izquierdo hacia la derecha
        return min_length if min_length != float('inf') else 0  # Si no se encontró una subarray válida, retorna 0

solution = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(solution.minSubArrayLen(target, nums))