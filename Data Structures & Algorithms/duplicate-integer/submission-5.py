class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a hashset of values
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False
