class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #idea: hashmap
        # n + n + n = 3n = O(n)
        count = {}
        #create an freq array that is length of the nums
        freq = [[] for i in range(len(nums) + 1)] 

        #get the count
        for n in nums:
            count[n] = 1 + count.get(n, 0) 
            #0 if doesnt exist in array yet
        #create freq table
        for n, c in count.items(): # for every key value pair 
            freq[c].append(n) # append n for every count

        res = []
        #get the k frequent, start from the higher freq to lower
        for i in range(len(freq) - 1, 0, -1):  
            for n in freq[i]: # look through the inner list at index
                res.append(n)
                if len(res) == k: # once we get k values: return
                    return res