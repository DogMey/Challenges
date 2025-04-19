class Solution(object):
    def jumps(self, nums):
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):  # No necesitamos procesar el último índice
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest        
        return jumps

solucion = Solution()

# Definir los saltos del arreglo
nums = [2,3,0,1,4]

print(solucion.jumps(nums))
