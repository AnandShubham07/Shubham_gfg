class Solution:
    def maxSubarraySum(self, arr, k):
        
        total=sum(arr[:k])
        max_sum=total
        for i in range(k,len(arr)):
                total=total-arr[i-k]+arr[i]
                max_sum=max(max_sum,total)
        return max_sum
