class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix and postfix optimal solution
        output = [1] * len(nums)

        prefix = 1 # left to right
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        #post fix r -> l
        postfix = 1 
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output

