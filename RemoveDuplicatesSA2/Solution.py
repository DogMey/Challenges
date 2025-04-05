class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        for i in range(len(nums)):
            if( k<2 or nums[k-2] != nums[i]):
                nums[k] = nums[i]
                k+=1
        print(nums)
        return k

solution = Solution()

# Ejemplo de uso
nums = [1,1,1,2,2,3]
k = solution.removeDuplicates(nums)