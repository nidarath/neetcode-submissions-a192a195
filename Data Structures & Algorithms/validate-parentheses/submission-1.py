class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # if this is a opening character
            if(char == "[" or char == "(" or char == "{"):
                stack.append(char)
            else:
                if(len(stack) == 0):
                    return False
                check = stack.pop()
                if(char == "]"):
                    if(check != "["):
                        return False
                if(char == ")"):
                    if(check != "("):
                        return False
                if(char == "}"):
                    if(check != "{"):
                        return False
        if(len(stack) != 0):
            return False
        return True