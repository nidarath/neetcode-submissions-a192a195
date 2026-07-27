class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
        #convert the number into binary, count the number of ones