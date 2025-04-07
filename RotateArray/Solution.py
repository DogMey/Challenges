class Solution(object):
    def rotar(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]  # Rotación usando slicing
        return nums

solucion = Solution()

# Definir los arreglos de entrada
nums = [1,2,3,4,5,6,7]
k = 3

print(solucion.rotar(nums, k))