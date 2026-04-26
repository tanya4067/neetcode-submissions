class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if(len(self.stack)!=0):
            self.stack.pop()
        

    def top(self) -> int:
        return(self.stack[-1])

        

    def getMin(self) -> int:
        min_value=2147483647
        for i in self.stack:
            if(i<min_value):
                min_value=i
        return(min_value)
        
