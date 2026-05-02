class Deque:
    
    def __init__(self):
        self.queue=[]


    def isEmpty(self) -> bool:
        if(len(self.queue)==0):
            return True
        return False
        

    def append(self, value: int) -> None:
        self.queue.append(value)
        

    def appendleft(self, value: int) -> None:
        self.queue.insert(0,value)
        

    def pop(self) -> int:
        if(len(self.queue)!=0):
            return(self.queue.pop())
        return(-1)
        
        

    def popleft(self) -> int:
        if(len(self.queue)!=0):
            return(self.queue.pop(0))
        return(-1)
        
