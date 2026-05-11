class Solution:
    def largest(self, arr):
        curr=arr[0]
        for i in range(0,len(arr)):
            if(arr[i]>curr):
                curr=arr[i]
        return curr
        
