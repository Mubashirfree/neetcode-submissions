class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        stack=Stack()
        oB=("(","{","[")
        cB=(")","}","]")

        for ch in s:
            if ch in oB:
                stack.push(ch)
            elif ch in cB:
                if (stack.peek()=="(" and ch==")") or (stack.peek()=="{" and ch=="}")or (stack.peek()=="[" and ch=="]"):
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