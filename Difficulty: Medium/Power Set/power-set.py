#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
    	list=[]
        def helper(s,index,curr):
            if(index==len(s)):
                list.append(curr)
                return 
            
            helper(s,index+1,curr+s[index])
           
            helper(s,index+1,curr)
        helper(s,0,"")
        list.sort()
        return list
    

	