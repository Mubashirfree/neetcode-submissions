class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch in ["+","-","*","/"]:
                secnum=stack.pop()
                firstnum=stack.pop()
                if ch =="+":
                    stack.append(firstnum+secnum)
                elif ch =="-":
                    stack.append(firstnum-secnum)
                elif ch =="*":
                    stack.append(firstnum*secnum)
                elif ch=="/":
                    stack.append(int(firstnum/secnum))
            else:
                stack.append(int(ch))
        ans=0
        while stack:
            ans+=stack.pop()
        return ans