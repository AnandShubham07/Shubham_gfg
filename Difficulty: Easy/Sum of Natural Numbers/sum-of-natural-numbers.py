#User function Template for python3

class Solution:
    def sumOfNaturals(self, n):
        if (n==1):
            return 1
        else:
            Nsum=n+self.sumOfNaturals(n-1)
            return Nsum
        