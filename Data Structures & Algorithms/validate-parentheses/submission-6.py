class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        openToClose={")":"(",
        "}":"{",
        "]":"["}
        for ch in s:
            if ch in openToClose:
                if stack and stack[-1]==openToClose[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if len(stack)==0 else False