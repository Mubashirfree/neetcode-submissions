class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        stack=Stack()
        paran={")":"(","}":"{","]":"["}

        for ch in s:
            if ch in paran.values():
                stack.push(ch)
            elif ch in paran.keys():
                if paran[ch]==stack.peek():
                    stack.pop()
                else:
                    return False
        return stack.isEmpty()



class Stack:
    def __init__(self):
        self.st=[]
        self.top=-1
    def isEmpty(self):
        return len(self.st)==0
    def push(self,x):
        self.st.append(x)
    def pop(self):
        if self.isEmpty():
            return 
        x=self.st[self.top]
        self.st.pop()
        return x
    def peek(self):
        if self.isEmpty():
            return
        return self.st[self.top]