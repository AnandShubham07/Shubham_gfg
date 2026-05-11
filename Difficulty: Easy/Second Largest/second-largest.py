class Solution:
    def getSecondLargest(self, arr):
        sl=-1
        curr=-1
        for i in range(0,len(arr)):
            if(arr[i]>curr):
                sl=curr
                curr=arr[i]
            elif(arr[i]<curr and arr[i]>sl):
               sl=arr[i]
        return sl
        
                
                