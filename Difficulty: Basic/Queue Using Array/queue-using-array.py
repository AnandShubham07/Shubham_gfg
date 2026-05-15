class myQueue:
    def __init__(self, n):
        self.arr=[]
        self.size=n
    
    def isEmpty(self):
        if(len(self.arr)!=0):
            return False
        else:
            return True
        
    def isFull(self):
        if(len(self.arr)==self.size):
            return True
        else:
            return False

    
    def enqueue(self, x):
        if not self.isFull():
            self.arr.append(x)

    
    def dequeue(self):
        if not self.isEmpty():
            self.arr.pop(0)

    
    def getFront(self):
        if not self.isEmpty():
            return self.arr[0]
        else:
            return -1
    
    def getRear(self):
        if not self.isEmpty():
            n=len(self.arr)
            return self.arr[n-1]
        else:
            return -1
            