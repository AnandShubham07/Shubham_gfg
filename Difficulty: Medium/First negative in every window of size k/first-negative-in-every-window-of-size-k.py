#User function Template for python3

         
from collections import deque
class Solution:
    def firstNegInt(self, arr, k):
        q = deque()
        res = []
    
        
        for i in range(k):
            if arr[i] < 0:
                q.append(i)
    
       
        for i in range(k, len(arr)):
    
            
            if q:
                res.append(arr[q[0]])
            else:
                res.append(0)
    
            
            while q and q[0] <= i - k:
                q.popleft()
    
           
            if arr[i] < 0:
                q.append(i)
    
       
        if q:
            res.append(arr[q[0]])
        else:
            res.append(0)
    
        return res