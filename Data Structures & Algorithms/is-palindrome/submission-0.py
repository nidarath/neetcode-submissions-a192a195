class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers 
        # one on the left and right comparing if same
        l, r  =  0, len(s) - 1

        while l < r:

            #skip white space
            while l < r and not s[l].isalnum(): 
                l += 1 

            while l < r and not s[r].isalnum():
                r -= 1 

            #if any not equal 
            # convert to lowercase for case sensitivity
            if s[l].lower() != s[r].lower():
                return False

            l += 1 #move the pointer to the right
            r -= 1 #move the pointer to the left

        return True 
