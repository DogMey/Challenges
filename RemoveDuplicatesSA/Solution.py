class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        k=0
        for i in range(len(nums)):
            if(nums[i] != nums[k]):
                k+=1
                nums[k] = nums[i]
        print(nums[:k+1])
        return k

solution = Solution()

# Ejemplo de uso
nums = [0,0,1,1,1,2,2,3,3,4]
k = solution.removeDuplicates(nums)