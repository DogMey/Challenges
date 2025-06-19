class Solution(object):
    def threeSum(self, nums):
        nums.sort()     # Se ordena la lista para facilitar la búsqueda
        result = []     # Lista para almacenar las tuplas que suman cero
        n = len(nums)   # Longitud de la lista nums
        for i in range(n - 2):                      # Recorremos hasta n-2 porque necesitamos al menos 3 números
            if i > 0 and nums[i] == nums[i - 1]:    # Evitamos duplicados para el primer número
                continue
            left, right = i + 1, n - 1              # Inicializamos dos punteros, uno al siguiente del actual y otro al final de la lista
            while left < right:                                     # Mientras los punteros no se crucen
                total = nums[i] + nums[left] + nums[right]          # Calculamos la suma de los tres números
                if total < 0:           # Si la suma es menor que cero, movemos el puntero izquierdo hacia la derecha
                    left += 1       
                elif total > 0:         # Si la suma es mayor que cero, movemos el puntero derecho hacia la izquierda
                    right -= 1
                else:                   # Si la suma es cero, hemos encontrado una tupla
                    result.append([nums[i], nums[left], nums[right]])       # Añadimos la tupla a la lista de resultados
                    while left < right and nums[left] == nums[left + 1]:    # Evitamos duplicados para el segundo número
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # Evitamos duplicados para el tercer número
                        right -= 1
                    left += 1   # Movemos ambos punteros para seguir buscando
                    right -= 1
        return result
    
nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))