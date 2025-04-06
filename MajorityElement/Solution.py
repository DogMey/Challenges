class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
# Crear una instancia de la clase Solution
solucion = Solution()

# Definir los arreglos de entrada
nums1 = [2,2,1,1,1,2,2]

# Imprimir a la función merge
print(solucion.majorityElement(nums1))