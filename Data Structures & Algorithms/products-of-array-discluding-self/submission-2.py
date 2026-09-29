class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #division solution
        """two of more zeros, res = all zeros
            one zero, only that position gets product of 0 
            no zeros, result[i] = total // nums[i]
            double divison, so u get integer
        """
        zcount = 0 # count of zeros
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zcount += 1
                continue # skip
            prod *= nums[i] # mult to running product

        # check zero counts
        if zcount > 1: # 2 or more zeros
            output = [0] * len(nums)
        elif zcount == 1: # one zero
            output = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = prod
        else: # no zeros
            output = [prod] * len(nums)
            for i in range(len(nums)):
                output[i] = output[i] // nums[i]
        return output
        
            
