class Solution(object):
    def canJump(self, nums):
        for i in range(len(nums)):
            if i > 0:
                nums[i] = max(nums[i], nums[i-1]-1)
            if nums[i] == 0 and i != len(nums)-1:
                return False
        return True
    
solucion = Solution()

# Definir los saltos del arreglo
nums = [2,3,1,1,4]

print(solucion.canJump(nums))