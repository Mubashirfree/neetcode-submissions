class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            minval=min(val,self.minstack[-1])
            self.minstack.append(minval)

    def pop(self) -> None:
        if self.stack:
            self.minstack.pop()
            return self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        
