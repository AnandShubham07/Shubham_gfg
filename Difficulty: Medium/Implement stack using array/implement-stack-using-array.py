class myStack:
    def __init__(self, n):
        self.size=n
        self.list=[]
    def isEmpty(self):
        if (len(self.list)!= 0):
            return False
        else:
            return True

    
    def isFull(self):
        if(len(self.list)==(self.size)):
           return True
        else:
            return False

    
    def push(self, x):
        if (len(self.list)!=self.size):
            self.list.append(x)
        else:
            self.isFull()
        
    def pop(self):
        if (len(self.list)==0):
           return -1
         
        else:
            self.list.pop()
        
        
    
    def peek(self):
        if not self.isEmpty():
            return self.list[-1]
        return -1