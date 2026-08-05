class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target = nums[i] + nums[j]
        #hashmap for quick lookup
        valMap = {} #where we store the value as the key & index as value


        for i, val in enumerate(nums):
            diff = target - val # difference is how we get nums[j]
            if diff in valMap: 
                return [valMap[diff], i] #return the indexes we found
            valMap[val] = i #else just add it to the hashmap
