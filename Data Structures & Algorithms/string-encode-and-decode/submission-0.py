class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # len#word
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1          #get end of word
            length = int(s[i:j]) #read this length
            res.append(s[j + 1 : j + 1 + length]) # append the word 
            i = j + 1 + length # move to new starting point
        return res