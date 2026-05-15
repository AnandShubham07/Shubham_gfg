class Solution:
    def sumOfDigits(self, n):
        
        rem=n//10
        if(rem==0):
            return n
        sum=n%10
        sum=sum+self.sumOfDigits(rem)
        return sum
        